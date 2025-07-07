# backend_whisperx.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import tempfile, os, gc, torch, whisperx, asyncio
from google import genai
from pydantic import BaseModel
import re
from google.genai import types
from openai import OpenAI

# ── configuration ───────────────────────────────────────────────────────────────
DEVICE        = "cuda"
MODEL_PATH    = "/home/arsalan77x/Whisper/chatwhisper-en-ct2"   # your ct2 model
COMPUTE_TYPE  = "float16"                                       # must match the ct2 files
HUGGING_FACE_TOKEN = "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"    # for diarization

# ── global models (loaded once) ────────────────────────────────────────────────
asr_model          = None
align_model        = None
align_metadata     = None
diarization_model  = None

openai_key = "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"
client = OpenAI(api_key=openai_key)
gen_client = genai.Client(api_key="AIzaSyBI5a5BNcHB3EwLfmRq3guzlrFMy1GYRPM")  
cfg = types.GenerateContentConfig(
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True           
    )
)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


class TextRequest(BaseModel):
    text: str
    
# ── helpers ────────────────────────────────────────────────────────────────────
def _pretty_dialogue(word_segments):
    """Turn word-level output into 'S0: ...' lines."""
    lines, cur_speaker, buf = [], None, []
    for w in word_segments:
            
        spk, word = w["speaker"], w["word"]
        if spk == "UNKNOWN_SPEAKER":
            spk = "SPEAKER_00"
        if spk != cur_speaker:
            if buf:
                label = f"S{int(cur_speaker.split('_')[-1])}"
                lines.append(f"{label}: " + " ".join(buf))
                buf = []
            cur_speaker = spk
        if word[0] in ".,;?!:" and buf:
            buf[-1] += word           # attach punctuation
        else:
            buf.append(word)
    if buf:
        label = f"S{int(cur_speaker.split('_')[-1])}"
        lines.append(f"{label}: " + " ".join(buf))
    return "\n".join(lines)


def _cast_word(w):
    """Convert non-serialisable types to plain Python for JSON."""
    word = ""
    if w["word"] == 'm':
        word = "mm"
    else:
        word = w["word"]

    return {
        "word":    str(word),
        "start":   float(w["start"]),
        "end":     float(w["end"]),
        "score":   float(w["score"]),
        "speaker": str(w.get("speaker", "UNKNOWN_SPEAKER")), # <--- MODIFIED HERE
    }


def transcribe_with_whisperx(wav_path: str):
    audio = whisperx.load_audio(wav_path)

    # 1️⃣  ASR
    result = asr_model.transcribe(audio, batch_size=4)
    segments = result["segments"]

    # 2️⃣  word-level alignment
    aligned = whisperx.align(segments, align_model, align_metadata,
                             audio, DEVICE, return_char_alignments=False)

    # 3️⃣  speaker diarisation
    diar_segments = diarization_model(audio, min_speakers=2, max_speakers=2)
    final = whisperx.assign_word_speakers(diar_segments, aligned)

    # 4️⃣  prepare outputs
    words = [_cast_word(w) for w in final["word_segments"]]

    dialogue = _pretty_dialogue(words)

    return {"words": words, "dialogue": dialogue}


# ── FastAPI lifecycle events ───────────────────────────────────────────────────
@app.on_event("startup")
async def load_models():
    global asr_model, align_model, align_metadata, diarization_model

    # Whisper / CTranslate2 model
    asr_model = whisperx.load_model(
        MODEL_PATH, device=DEVICE, language="en", compute_type=COMPUTE_TYPE
    )

    # Alignment model (tiny, stays on GPU)
    align_model, align_metadata = whisperx.load_align_model(
        language_code="en", device=DEVICE
    )

    # Pyannote diarisation pipeline (CPU by default, set device="cuda" if you
    # have enough VRAM; turn off chunk batching to save memory)
    diarization_model = whisperx.diarize.DiarizationPipeline(
        use_auth_token=HUGGING_FACE_TOKEN, device=DEVICE
    )


@app.on_event("shutdown")
async def unload_models():
    # optional – free GPU/CPU RAM when server stops
    global asr_model, align_model, diarization_model
    del asr_model, align_model, diarization_model
    gc.collect()
    torch.cuda.empty_cache()


# ── routes ─────────────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def index():
    try:
        return HTMLResponse(open("static/index.html").read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="index.html not found")



@app.post("/analyze")
async def fix_grammar(request: TextRequest):
    input_text = request.text
    # STEP 1: utterance
    pattern = re.compile(r'\b(uh|um|mhmm|mhm|mm)\b[.,!?]?')
    input_text = pattern.sub(lambda m: '&-' + m.group(1), input_text)

    # STEP 2: Grammar
    try:
        prompt = f"""
        The text below is from a conversation with an aphasic speaker. Preserve all filler utterances (e.g. “uh”, “um”)—do not remove them. Minor grammar slips are expected and may be ignored, but correct any serious errors. **Also, identify and correct any spelling errors.** For each correction, keep the original mistaken text inline using this format: 
        [+ gram] #(original text) 
        **For spelling errors, use this format: [: original_wrong_word] corrected_word**

        Your output should return only the corrected conversation, with corrections and inline error markers, and no other commentary.

        Here is the text to correct:

        {input_text}

        Example:

        input:
        S1: could you tell me about it?
        S0: &-Uh it was late in December. I was alone in my small house behind my &-uh &-uh a friend from my daughters. and &-um santa Cause ...

        output:
        S1: could you tell me about it?
        S0: &-Uh it was late in December. I was alone in my small house, [+ gram] #(behind my &-uh &-uh a friend from my daughters) behind the house of a friend of my daughter’s. and &-um Santa [: Cause] Claus...
        """

        response = gen_client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=prompt,
            config=cfg,
        )

     
        output = response.text
        return {"corrected_text": output}
    except Exception as e:
        return {"error": str(e)}

@app.post("/transcribe")
async def transcribe_endpoint(file: UploadFile = File(...)):
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Please upload an audio file")

    # save upload to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        out = await asyncio.to_thread(transcribe_with_whisperx, tmp_path)
        return JSONResponse(content=out)
    finally:
        os.unlink(tmp_path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
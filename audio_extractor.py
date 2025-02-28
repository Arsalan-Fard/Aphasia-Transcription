from pydub import AudioSegment
import os

def chunk_wav_file(input_file, output_folder, chunk_length=5*60*1000):  # 5 minutes in milliseconds
    # Load the audio file
    audio = AudioSegment.from_wav(input_file)

    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Split the audio into chunks
    num_chunks = len(audio) // chunk_length + (1 if len(audio) % chunk_length != 0 else 0)

    for i in range(num_chunks):
        start_time = i * chunk_length
        end_time = min((i + 1) * chunk_length, len(audio))
        
        chunk = audio[start_time:end_time]
        chunk_name = os.path.join(output_folder, f"chunk_{i+1}.wav")
        
        chunk.export(chunk_name, format="wav")
        print(f"Saved: {chunk_name}")

    print("Audio chunking completed!")

# Example usage
input_wav = "Dataset/Audio/1554.wav"  # Change to your file path

output_dir = "1554_chunks"  # Directory to save chunks

chunk_wav_file(input_wav, output_dir)

# from google import genai
# from pydantic import BaseModel
# import re
# from google.genai import types
# gen_client = genai.Client(api_key="AIzaSyBI5a5BNcHB3EwLfmRq3guzlrFMy1GYRPM")
# cfg = types.GenerateContentConfig(
#     automatic_function_calling=types.AutomaticFunctionCallingConfig(
#         disable=True           
#     )
# )
# myfile = gen_client.files.upload(file='1.mp3')
# prompt = 'Generate a transcript of the speech.'

# response = gen_client.models.generate_content(
#   model="gemini-2.5-flash-preview-05-20",
#   contents=[prompt, myfile]
# )

# print(response.text)





# from pydub import AudioSegment
# import os

# def convert_wav_to_mp3(wav_file_path):
#     """
#     Converts a .wav file to a .mp3 file.

#     Args:
#         wav_file_path (str): The path to the input .wav file.
#     """
#     if not os.path.exists(wav_file_path):
#         print(f"Error: WAV file not found at '{wav_file_path}'")
#         return

#     try:
#         audio = AudioSegment.from_wav(wav_file_path)

#         # Generate the output MP3 file path
#         base_name = os.path.splitext(wav_file_path)[0]
#         mp3_file_path = f"{base_name}.mp3"

#         audio.export(mp3_file_path, format="mp3")
#         print(f"Successfully converted '{wav_file_path}' to '{mp3_file_path}'")

#     except Exception as e:
#         print(f"An error occurred during conversion: {e}")

# if __name__ == "__main__":
#     wav_file = "1.wav"  # Your WAV file name
#     convert_wav_to_mp3(wav_file)
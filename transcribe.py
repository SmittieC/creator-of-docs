import whisper

def transcribe_audio(audio_path, context):
    whisper_prompt = f"{context}"
    model = whisper.load_model("large")
    print("Transcribing")
    transcription = model.transcribe(audio_path, initial_prompt=whisper_prompt)
    print(f"Done. Saving transcription.")
    with open('text.txt', 'w') as file:
        file.write(transcription['text'])

if __name__ == "__main__":
    audio_path = input("Name of the audio file:\n")
    audio_context = input("""(Optional) Provide some context for the audio. This helps detect certain words:\n""")
    transcribe_audio(audio_path=audio_path, context=audio_context)
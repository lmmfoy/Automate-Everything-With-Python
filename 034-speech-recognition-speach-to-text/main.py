from speech_recognition import Recognizer, AudioFile

recognizer = Recognizer()

with AudioFile("034-speech-recognition-speach-to-text/chile.wav") as audio_file:
    # Record audio of audiofile 
    audio = recognizer.record(audio_file)

# Using Google speech recognition API
text = recognizer.recognize_google(audio)
print(text)
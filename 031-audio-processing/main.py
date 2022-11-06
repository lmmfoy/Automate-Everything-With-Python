from pydub import AudioSegment

AudioSegment.converter = "C:/FFmpeg/bin/ffmpeg"

original_audio = AudioSegment.from_wav("031-audio-processing/beat.wav")

# Reverse audio file, louder by 15 decibels
reversed_audio = original_audio.reverse()
print(reversed_audio)
reversed_audio.export("031-audio-processing/reversed.wav")
reversed_audio = reversed_audio + 15

# Slice audio file - expects miliseconds
first_two_sec = original_audio[0:2000]
first_two_sec.export("031-audio-processing/first_two_sec.wav")

# Length of audio file
print(len(original_audio))

# Merge 2 audio files with original audio playing twice, then 1 second silence, then second audio  
merged_audio = original_audio * 2 + AudioSegment.silent(1000) + reversed_audio
merged_audio.export("031-audio-processing/merged_audio.wav")
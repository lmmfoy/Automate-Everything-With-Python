from pydub import AudioSegment

AudioSegment.converter = "C:/FFmpeg/bin/ffmpeg"

beat = AudioSegment.from_wav("031-overlaying-mixing-audio/beat.wav")
sax = AudioSegment.from_wav("031-overlaying-mixing-audio/sax.wav")

beat2 = beat * 2
beat2.export("031-overlaying-mixing-audio/beat2.wav")

# Overlay one audio on top of another
mixed = beat2.overlay(sax)
mixed.export("031-overlaying-mixing-audio/mixed.wav")

final = beat2 * 2 + mixed + beat2 + mixed + sax 
final.export("031-overlaying-mixing-audio/final.wav")
from pydub import AudioSegment

AudioSegment.converter = "C:/FFmpeg/bin/ffmpeg"

beat = AudioSegment.from_wav("033-adding-audio-effects-filter-mono-stereo/beat.wav")

# Apply low pass filter to remove high frequencies
# Must specify frequency (above 2000 will be removed)
beat_low = beat.low_pass_filter(2000)
beat_low.export("033-adding-audio-effects-filter-mono-stereo/beat_low.wav")

# Mono effect
# For left speaker: -1; For right: 1. (-0.5 will be more on left, less on right)
beat_left = beat_low.pan(-1)
beat_right = beat_low.pan(1)

beat_final = beat_left + beat_right + beat_low
beat_final.export("033-adding-audio-effects-filter-mono-stereo/beat_final.wav")
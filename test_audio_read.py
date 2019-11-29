import miniaudio
stream = miniaudio.stream_file("test_audio.mp3")
device = miniaudio.PlaybackDevice()
device.start(stream)
input("Audio file playing in the background. Enter to stop playback: ")
device.close()

# sudo apt-get install ffmpeg

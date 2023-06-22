from pytube import YouTube
import os

while(True):
    url = str(input("Enter the url. Enter 'quit' to exit.\n>>"))

    if url.lower() == 'quit':
        print("Program exited.")
        break

    yt = YouTube(url)
    audio = yt.streams.get_audio_only()
    music = audio.download()
    os.rename(music, yt.title + ".mp3")
    print(yt.title + " downloaded.")

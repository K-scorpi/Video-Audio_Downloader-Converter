import moviepy.editor
from pytube import YouTube
import os


def video_downloader(ref):
    yt = YouTube(ref)  # link
    yt.streams.filter(progressive=True, file_extension='mp4')\
        .order_by('resolution').desc()\
        .first().download('Videos') #'Videos'

    name = str(yt.title)

    def audio_capture(file):
        n1 = str(f'Videos/{file}.mp4')
        n2 = str(f'Videos/{file}.mp3')
        video = moviepy.editor.VideoFileClip(n1) #name
        clip_audio = video.audio
        clip_audio.write_audiofile(n2)
        video.close()
        clip_audio.close()

    #def deletion():
    #    os.remove(f'Videos/{name}.mp4')
    #    os.remove(f'Videos/{name}.mp3')

    audio_capture(name)
    #deletion()

video_downloader(input()) #input()

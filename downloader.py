from pytube import YouTube
from moviepy.editor import *
import os, sys


class Downloader():

    # Only Video
    def download_video_highest_res(self, url, output_path):
        try:
            yt = YouTube(url, on_progress_callback=self.progress_function)

            # Choosing the best video only stream
            video_stream = yt.streams.filter(only_video=True, file_extension='mp4').order_by('resolution').desc().first()

            if output_path:
                video_stream.download(output_path)
            else:
                video_stream.download()

            print(f"Audio has been downloaded successfully {yt.title}")
        except Exception as e:
            print(f"An error has been occured: {e}")


    # Only Audio
    def download_audio(self, url, output_path):
        try:
            # Creating the object with the url
            yt = YouTube(url, on_progress_callback=self.progress_function)
            
            # Getting the audio
            audio = yt.streams.filter(only_audio=True).first()
            
            # Downloading the audio
            if output_path:
                audio.download(output_path)
            else:
                audio.download()

            print(f"Audio has been downloaded successfully {yt.title}")
        except Exception as e:
            print(f"An error has been occured: {e}")


    # Video with audio
    def video_with_audio(self, url, output_path):

        try:
            # Creating the object with the url
            yt = YouTube(url, on_progress_callback=self.progress_function)
            
            # Getting the highest resolution as possible
            video = yt.streams.get_highest_resolution()
            
            # Downloading the video
            if output_path:
                video.download(output_path)
            else:
                video.download()

            print(f"Video has been downloaded successfully {yt.title}")
        except Exception as e:
            print(f"An error has been occured: {e}")



    def progress_function(self, stream, chunk, bytes_remaining):

        # Total file size
        total_size = stream.filesize

        # Downloaded bytes
        bytes_downloaded = total_size - bytes_remaining

        # Calculatin the percentage
        percentage_of_completion = bytes_downloaded / total_size * 100

        # Printing the percentage
        print(f'{int(percentage_of_completion)}%')
        self.percentage = f'{int(percentage_of_completion)}%'
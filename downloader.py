from pytube import YouTube
import os, sys


class Downloader():

    def download_video_highest_res(self, url):
        try:
            # Creating the object with the url
            yt = YouTube(url, on_progress_callback=self.progress_function)
            
            # Getting the highest resolution as possible
            video = yt.streams.get_highest_resolution()
            
            # Downloading the video
            video.download()
            print(f"Video has been downloaded successfully {yt.title}")
        except Exception as e:
            print(f"An error has been occured: {e}")


    def download_audio(self, url):
        try:
            # Creating the object with the url
            yt = YouTube(url, on_progress_callback=self.progress_function)
            
            # Getting the audio
            audio = yt.streams.filter(only_audio=True).first()
            
            # Downloading the audio
            audio.download()
            print(f"Audio has been downloaded successfully {yt.title}")
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
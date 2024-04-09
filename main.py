from downloader import Downloader

download = Downloader()

video_link = input('Give me a link:\n')
choice = input('[A]-Audio   [V]-Video\n')

choice = choice.lower()
if choice == 'a':
    download.download_audio(video_link)
elif choice == 'v':
    download.download_video_highest_res(video_link)
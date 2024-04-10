from downloader import Downloader

download = Downloader()

video_link = input('Give me a link:\n')
output_path = input('Where to download? (default setting is the current folder)')
choice = input('[A]-Audio   [V]-Video   [B]-Both\n')

choice = choice.lower()
if choice == 'a':
    download.download_audio(video_link, output_path)
elif choice == 'v':
    download.download_video_highest_res(video_link, output_path)
elif choice == 'b':
    download.video_with_audio(video_link, output_path)
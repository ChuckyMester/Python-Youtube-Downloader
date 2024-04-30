from tiktok import TikTok_Downloader
import asyncio
import os


async def main():

    download = TikTok_Downloader()

    link = input("Paste the link here:\n")

    await download.download_video(link)



main()
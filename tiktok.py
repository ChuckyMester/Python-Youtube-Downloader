from TikTokApi import TikTokApi
import asyncio
import os


class TikTok_Downloader:

    def __init__(self):

        self.ms_token = os.environ.get(
            "ms_token", None
        )


    async def get_video_example(self, url):
        async with TikTokApi() as api:
            await api.create_sessions(ms_tokens=[self.ms_token], num_sessions=1, sleep_after=3)
            video = api.video(
                url=url
            )

            video_info = await video.info()
            download_url = video_info['video']['downloadAddr']
            print(download_url)



download = TikTok_Downloader()
url = input('Give me a link:\n')
if __name__ == "__main__":
    asyncio.run(download.get_video_example(url))

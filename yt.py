import logging
from dataclasses import dataclass
from datetime import datetime

from googleapiclient.discovery import build

API_KEY = "AIzaSyD0PDzc7yTNn-GfXvS52KpI2LRzdJnW848"


@dataclass
class Video:
    title: str
    description: str
    thumbnail_url: str
    published_at: str


def get_yt_videos():

    youtube = build("youtube", "v3", developerKey=API_KEY)

    request = youtube.search().list(
        q="fifa",
        part="snippet",
        type="video",
        order="date",
        # maxResults=1,
        publishedAfter=datetime.utcfromtimestamp((datetime.now().timestamp())).strftime(
            "%Y-%m-%dT%H:%M:%S.0Z"
        ),
    )

    response = request.execute()
    list_of_videos = []
    for search_result in response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            try:
                snippet = search_result["snippet"]
                video = Video(
                    snippet["title"],
                    snippet["description"],
                    snippet["thumbnails"]["medium"]["url"],
                    snippet["publishedAt"],
                )
                list_of_videos.append(video)
            except Exception as exception:
                logging.getLogger(__name__).exception(exception)

    return list_of_videos


print(get_yt_videos())
# service.close()

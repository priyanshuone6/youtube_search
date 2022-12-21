import logging
import os
from dataclasses import dataclass
from datetime import datetime

from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


@dataclass
class Video:
    """Model class to return video object"""

    title: str
    description: str
    thumbnail_url: str
    published_at: str


def get_yt_videos():
    """
    Get YouTube videos from the API and return a list of video objects having title,
    description, thumbnail url and published date and time of the video.
    """

    # Uses YouTube v3 API to get videos (https://developers.google.com/youtube/v3/docs/search/list)
    youtube = build("youtube", "v3", developerKey=API_KEY)

    # Get all the videos uploaded at given time
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

    # Create a list of video objects from the model class
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

            # Log the exception if any
            except Exception as exception:
                logging.getLogger(__name__).exception(exception)

    return list_of_videos


# service.close()

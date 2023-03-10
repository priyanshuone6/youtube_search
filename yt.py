# Description: This file contains the code to get YouTube videos from the API.

import logging
import os
import time
from dataclasses import dataclass
from datetime import datetime

import dotenv
from googleapiclient.discovery import build

import db

# Load environment variables from .env file
dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")


@dataclass
class Video:
    """Model class to return video object"""

    title: str
    description: str
    thumbnail_url: str
    published_at: str


DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def get_yt_videos(publishedAfter):
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
        publishedAfter=publishedAfter,
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


def call_yt_interval():

    # Create database object
    db_obj = db.PostgresDB()

    # Call the function to get videos
    while True:
        # Get latest timestamp from database
        timestamp = db_obj.get_max_timestamp() or datetime.utcnow().strftime(
            DATE_FORMAT
        )
        # Get videos from YouTube API at given timestamp
        videos = get_yt_videos(timestamp)
        # Insert videos into database
        db_obj.insert_videos(videos)

        # Sleep for 10 seconds
        time.sleep(10)


if __name__ == "__main__":
    call_yt_interval()

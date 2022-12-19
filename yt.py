from datetime import datetime

from googleapiclient.discovery import build

API_KEY = "AIzaSyD0PDzc7yTNn-GfXvS52KpI2LRzdJnW848"

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

print(response)

# service.close()

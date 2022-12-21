import os

import psycopg2
from dotenv import load_dotenv

import yt

# Load environment variables from .env file
load_dotenv()
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

# Connect to the database
con = psycopg2.connect(
    host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT
)

# Create a cursor
cursor = con.cursor()

# Create table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS videos (id SERIAL PRIMARY KEY, title VARCHAR(255), description VARCHAR(255), thumbnail_url VARCHAR(255), publishing_datetime TIMESTAMP)"
)

# Create index on publishing_datetime column in descending order
cursor.execute(
    "CREATE INDEX IF NOT EXISTS idx_videos_publishing_datetime ON videos (publishing_datetime DESC)"
)

# Loop through the list of videos and insert them into the database
for video in yt.get_yt_videos():
    cursor.execute(
        "INSERT INTO videos (title, description, thumbnail_url, publishing_datetime) VALUES (%s, %s, %s, %s)",
        (video.title, video.description, video.thumbnail_url, video.published_at),
    )


# Close the cursor
cursor.close()

# Close the connection
con.close()

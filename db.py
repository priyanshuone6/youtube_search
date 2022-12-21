# Description: This file contains the code to create a database table and insert data into it.

import os
from itertools import chain

import dotenv
import psycopg2

# Load environment variables from .env file
dotenv.load_dotenv()
DATABASE = os.getenv("DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


class PostgresDB:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=HOST, database=DATABASE, user=DB_USER, password=DB_PASSWORD, port=PORT
        )
        self.cursor = self.connection.cursor()

        # Create table and index
        self.create_table()
        self.create_index()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS videos (id SERIAL PRIMARY KEY, title VARCHAR(255), description VARCHAR(255), thumbnail_url VARCHAR(255), publishing_datetime TIMESTAMP)"
        )

    def create_index(self):
        self.cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_videos_publishing_datetime ON videos (publishing_datetime DESC)"
        )

    def insert_videos(self, videos):

        # videos = get_yt_videos();
        if videos:
            query = (
                "INSERT INTO videos (title, description, thumbnail_url, publishing_datetime) VALUES"
                + ",".join(["(%s, %s, %s, %s)"] * len(videos))
                + ";"
            )
            self.cursor.execute(
                query,
                list(
                    chain(
                        *[
                            (
                                video.title,
                                video.description,
                                video.thumbnail_url,
                                video.published_at,
                            )
                            for video in videos
                        ]
                    )
                ),
            )

    def get_all_videos(self):
        self.cursor.execute("SELECT * FROM videos")
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
        self.connection = None

    def get_max_timestamp(self):
        self.cursor.execute("SELECT MAX(publishing_datetime) FROM videos")
        return self.cursor.fetchone()[0]

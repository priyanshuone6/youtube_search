# Description: This file contains the code to create a database table and insert data into it.

import os
from contextlib import contextmanager
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
        # Create table and index
        self.create_table()
        self.create_index()

    @contextmanager
    def connect(self):
        with psycopg2.connect(
            host=HOST, database=DATABASE, user=DB_USER, password=DB_PASSWORD, port=PORT
        ) as conn:
            with conn.cursor() as cursor:
                yield cursor

    def create_table(self):
        with self.connect() as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS videos (id SERIAL PRIMARY KEY, title VARCHAR(255), description VARCHAR(255), thumbnail_url VARCHAR(255), publishing_datetime VARCHAR(255))"
            )

    def create_index(self):
        with self.connect() as cursor:
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_videos_publishing_datetime ON videos (publishing_datetime DESC)"
            )

    def insert_videos(self, videos):

        if not videos:
            return

        with self.connect() as cursor:
            query = (
                "INSERT INTO videos (title, description, thumbnail_url, publishing_datetime) VALUES"
                + ",".join(["(%s, %s, %s, %s)"] * len(videos))
                + ";"
            )
            cursor.execute(
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

    def get_videos(self, after=0, num_items=0):
        with self.connect() as cursor:
            cursor.execute(
                "SELECT * FROM videos WHERE %s < publishing_datetime ORDER BY publishing_datetime DESC LIMIT %s",
                (after, num_items),
            )
            return cursor.fetchall()

    def get_max_timestamp(self):
        with self.connect() as cursor:
            cursor.execute("SELECT MAX(publishing_datetime) FROM videos")
            timestamp = cursor.fetchone()[0]

            return timestamp

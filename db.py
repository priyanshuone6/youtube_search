import psycopg2

import yt

DATABASE = "test_app"
USER = "postgres"
PASSWORD = "1234"
HOST = "localhost"
PORT = "5432"


# Connect to the database
con = psycopg2.connect(
    host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT
)

# Create a cursor
cursor = con.cursor()


# create table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS videos (id SERIAL PRIMARY KEY, title VARCHAR(255), description VARCHAR(255), thumbnail_url VARCHAR(255), publishing_datetime TIMESTAMP)"
)

cursor.execute(
    "CREATE INDEX IF NOT EXISTS idx_videos_publishing_datetime ON videos (publishing_datetime DESC)"
)

for video in yt.get_yt_videos():
    cursor.execute(
        "INSERT INTO videos (title, description, thumbnail_url, publishing_datetime) VALUES (%s, %s, %s, %s)",
        (video.title, video.description, video.thumbnail_url, video.published_at),
    )


# Close the cursor
cursor.close()

# Close the connection
con.close()

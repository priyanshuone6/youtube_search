# Description: This file is the main file for the Flask app

from flask import Flask, request

import db
import yt

# Create Flask app
app = Flask(__name__)

# Create database object
db_obj = db.PostgresDB()


@app.route("/")
def index():
    return "access GET /videos to get latest uploaded fifa videos."


@app.route("/videos")
def get_videos():
    # Get query params
    after = request.args.get("after")

    # Validate query params
    if after is None:
        return f"Query param 'after' in the format {yt.DATE_FORMAT} is required", 400

    # Get optional query params
    num_items = request.args.get("num_items", 1, int)

    # Execute query to get all videos
    videos = db_obj.get_videos(after=after, num_items=num_items)

    return [yt.Video(*video[1:]) for video in videos]


if __name__ == "__main__":
    # Run server
    app.run(debug=True)  # to allow for debugging and auto-reload

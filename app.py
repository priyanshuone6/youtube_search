# Description: This file is the main file for the Flask app

from flask import Flask, request

import db

# Create Flask app
app = Flask(__name__)

# Create database object
db_obj = db.PostgresDB()


@app.route("/data")
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get("user")


@app.route("/videos")
def index():
    after = request.args.get("after", 0, int)
    num_items = request.args.get("num_items", 0, int)
    # Execute query to get all videos
    videos = db_obj.get_all_videos(after=after, num_items=num_items)
    return [videos, after, num_items]


if __name__ == "__main__":
    # Run server
    app.run(debug=True)  # to allow for debugging and auto-reload

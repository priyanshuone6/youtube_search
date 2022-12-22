# 🔎 YouTube Search
YouTube Search is an API that retrieves the most recent videos from YouTube for a specified tag or search query, paginated and ordered in reverse chronological order of their publishing date-time.

## 📚 Tech Stack
- Python
- PostgreSQL
- Flask

## 📋 Requirements
- Python 3.7 or higher
- PostgreSQL

## 📦 Installation
- Install the requirements using the following command:

```bash
pip install -r requirements.txt
```

- Install PostgreSQL (see [here](https://www.postgresql.org/download/) for instructions)
- Create a database in PostgreSQL
- Update YouTube API key and database credentials environment variables in the file named `.env`.

## 📁 Project structure
```
                         ┌─── app.py ────── Main flask app
                         │
                         │
┌──────────────┐         ├─── yt.py ─────── Gets YouTube videos from the API
│YouTube_Search├─────────┤
└──────────────┘         │
                         ├─── db.py ─────── PostgresSQL database
                         │
                         │
                         └─── .env ──────── Environment variables
```

## 🚀 Running the project
- Clone the repository
- Run the flask app using the following command:

```bash
flask run
```

- Also run the Youtube Search cron method using the following command:

```bash
python yt.py
```

- Access GET `/videos` to get latest uploaded videos from YouTube and query parameter `after` in the format `%Y-%m-%dT%H:%M:%SZ`. By default it returns the latest one videos. You can also specify the number of items to be returned using the query parameter `num_items`.
For example:
`http://127.0.0.1:5000/videos?after=2022-12-22T13:40:10Z&num_items=3`

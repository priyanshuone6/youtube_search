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
- Add environment variables in a file named `.env`.

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

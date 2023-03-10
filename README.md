# π YouTube Search
YouTube Search is an API that retrieves the most recent videos from YouTube for a specified tag or search query, paginated and ordered in reverse chronological order of their publishing date-time.

## π Tech Stack
- Python
- PostgreSQL
- Flask

## π Requirements
- Python 3.7 or higher
- PostgreSQL

## π¦ Installation
- Install the requirements using the following command:

```bash
pip install -r requirements.txt
```

- Install PostgreSQL (see [here](https://www.postgresql.org/download/) for instructions)
- Create a database in PostgreSQL
- Update YouTube API key and database credentials environment variables in the file named `.env`.

## π Project structure
```
                         ββββ app.py ββββββ Main flask app
                         β
                         β
ββββββββββββββββ         ββββ yt.py βββββββ Gets YouTube videos from the API
βYouTube_Searchβββββββββββ€
ββββββββββββββββ         β
                         ββββ db.py βββββββ PostgresSQL database
                         β
                         β
                         ββββ .env ββββββββ Environment variables
```

## π Running the project
- Clone the repository
- Start the PostgreSQL server

- Run the background process to get YouTube videos and store them in the database using the following command:
```bash
python yt.py
```

- Also run the flask app using the following command:

```bash
flask run
```

- Access GET `/videos` to get latest uploaded videos from YouTube sorted in descending order by their published date time. It accepts two query parameter
  - `after`: (required) date time after which videos are to be returned. It should be in the format `%Y-%m-%dT%H:%M:%SZ`.
  - `num_items`: (optional) number of items to be returned, default is one.

For example:
`http://127.0.0.1:5000/videos?after=2022-12-22T13:40:10Z&num_items=3`

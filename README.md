# YouTube Search
YouTube Search is an API that retrieves the most recent videos from YouTube for a specified tag or search query, paginated and ordered in reverse chronological order of their publishing date-time.

## Requirements
- Python 3.7+
- PostgreSQL

## Installation and setting up
- Install the requirements using the following command:

```bash
pip install -r requirements.txt
```

- Install PostgreSQL (see [here](https://www.postgresql.org/download/) for instructions)
- Create a database in PostgreSQL
- Add environment variables in a file named `.env`.

## Running the project
- Clone the repository
- Run the django server

```bash
python manage.py runserver
```

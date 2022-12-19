import sqlalchemy

from google.cloud.sql.connector import Connector

# initialize parameters
INSTANCE_CONNECTION_NAME = "youtube-api-372117:europe-north1:postgresql-db"  # i.e demo-project:us-central1:demo-instance

DB_USER = "quickstart-user"
DB_PASS = "admin"
DB_NAME = "postgresql-db"


# initialize Connector object
connector = Connector()

# function to return the database connection object
def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME, "pg8000", user=DB_USER, password=DB_PASS, db=DB_NAME
    )
    return conn


# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)


# Query################


# connect to connection pool
with pool.connect() as db_conn:
    # create ratings table in our movies database
    db_conn.execute(
        "CREATE TABLE IF NOT EXISTS ratings "
        "( id SERIAL NOT NULL, title VARCHAR(255) NOT NULL, "
        "genre VARCHAR(255) NOT NULL, rating FLOAT NOT NULL, "
        "PRIMARY KEY (id));"
    )
    # insert data into our ratings table
    insert_stmt = sqlalchemy.text(
        "INSERT INTO ratings (title, genre, rating) VALUES (:title, :genre, :rating)",
    )

    # insert entries into table
    db_conn.execute(insert_stmt, title="Batman Begins", genre="Action", rating=8.5)
    db_conn.execute(
        insert_stmt, title="Star Wars: Return of the Jedi", genre="Action", rating=9.1
    )
    db_conn.execute(insert_stmt, title="The Breakfast Club", genre="Drama", rating=8.3)

    # query and fetch ratings table
    results = db_conn.execute("SELECT * FROM ratings").fetchall()

    # show results
    for row in results:
        print(row)

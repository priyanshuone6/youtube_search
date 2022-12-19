import psycopg2

# Connect to the database
con = psycopg2.connect(
    host="localhost", database="yttest", user="postgres", password="postgres"
)


# Create a cursor
cur = con.cursor()

# Execute a query
cur.execute("select id, name from test")

rows = cur.fetchall()

for row in rows:
    print(row)

# Close the cursor
cur.close()

# Close the connection
con.close()

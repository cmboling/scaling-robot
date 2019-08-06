
# part 1
import psycopg2

connection = psycopg2.connect("dbname=dq user=dq")

print(connection)

connection.close()

# part 2
import psycopg2

ourConnection = psycopg2.connect("dbname=dq user=dq")
ourCursor = ourConnection.cursor()
ourCursor.execute("SELECT * FROM notes")

notes = ourCursor.fetchall()
one = ourCursor.fetchone()
ourConnection.close()

# part 3
import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""
                CREATE TABLE users(
                    id INTEGER PRIMARY KEY,
                    email TEXT,
                    name TEXT,
                    address TEXT
                )
            """
           )


# part 4
import psycopg2 as pc2

conn = pc2.connect("dbname=dq user=dq")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute(""" 
                CREATE TABLE users(
                    id INTEGER PRIMARY KEY,
                    email text,
                    name text,
                    address text
                )
            """)

conn.commit()
conn.close()


# part 5
import psycopg2 as pc2
import csv as csv


# establish connection and cursor   
conn = pc2.connect("dbname=dq user=dq")
cur = conn.cursor()  

# load csv
with open('user_accounts.csv','r') as f:
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        print(line)
        cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s)",line)

# commit queries
conn.commit()

# fetch records from users table
cur.execute("SELECT * FROM users")
users = cur.fetchall()

# close connection
conn.close()


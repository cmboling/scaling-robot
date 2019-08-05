
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
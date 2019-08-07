
# 1 creating tables

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

cur.execute('SELECT * FROM ign_reviews LIMIT 0')
print(cur.description)


# 2 creating tables

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

cur.execute(
    """
        CREATE TABLE ign_reviews(
        
        id BIGINT PRIMARY KEY
        
        )
    """
)

conn.commit()

# 3 creating tables

# print next column

import csv
with open('ign.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    unique_words_in_score_phrase = set([
        row[1] for row in reader
    ])

print(unique_words_in_score_phrase)


# finding max length

import csv

with open('ign.csv','r') as f:
    next(f)
    reader = csv.reader(f)
    score_lengths = [len(row[1]) for row in reader]
    max_score = max(score_lengths)
    


# part 4 creating tables
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS ign_reviews")

cur.execute(
    """ 
    CREATE TABLE ign_reviews(
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11)
    
    )
    
    """
)

conn.commit()


# part 5/6
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE ign_reviews (
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11),
        title TEXT,
        url TEXT,
        platform VARCHAR(20),
        genre TEXT,
        score DECIMAL(3, 1)
    )
""")
conn.commit()


# part 7
conn = psycopg2.connect("dbname=dq user=dq")

cur.execute("""
    CREATE TABLE ign_reviews (
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11),
        title TEXT,
        url TEXT,
        platform VARCHAR(20),
        score DECIMAL(3, 1),
        genre TEXT,
        editors_choice BOOLEAN
    )
""")
conn.commit()


# part 8 - dates
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

import csv
from datetime import date
cur.execute("""
    CREATE TABLE ign_reviews (
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11),
        title TEXT,
        url TEXT,
        platform VARCHAR(20),
        score DECIMAL(3, 1),
        genre TEXT,
        editors_choice BOOLEAN,
        release_date DATE
    )
""")

with open('ign.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    for row in reader:
        updated_row = row[:8]
        updated_row.append(date(int(row[8]), int(row[9]), int(row[10])))
        cur.execute("INSERT INTO ign_reviews VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", updated_row)
conn.commit()

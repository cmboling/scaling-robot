# part 1
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('ALTER TABLE old_ign_reviews RENAME TO ign_reviews')
conn.commit()
cur.execute('SELECT * FROM ign_reviews LIMIT 0')
print(cur.description)

# part 2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('ALTER TABLE ign_reviews DROP COLUMN full_url')
conn.commit()

# part 3 
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('ALTER TABLE ign_reviews ALTER COLUMN id TYPE BIGINT')
conn.commit()
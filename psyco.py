import psycopg2



#connect to the db
con = psycopg2.connect(
    host = 'localhost',
    database = 'Music_Library',
    user = "WarrenB",
)

cur = con.cursor()

cur.execute('select * from songs')

cur.close()

for r in rows:
    print (f"id {r[0]} artist {r[1]}")

rows = cur.fetchall()

#close the db connection
con.close()
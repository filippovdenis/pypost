import psycopg2

DSN = 'postgres://postgres:tamplier@localhost'

conn = psycopg2.connect(DSN)
print(conn)

cur = conn.cursor()

cur.execute("select datname from pg_database")

for row in cur:
    (datname,) = row
    print(datname)
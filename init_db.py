import sqlite3

conn = sqlite3.connect("evoting.db")

with open("schema.sql", "r") as f:
    sql = f.read()

conn.executescript(sql)
conn.commit()
conn.close()

print("Database ready")

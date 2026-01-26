import sqlite3

conn = sqlite3.connect("kanpur_metro.db")
cur = conn.cursor()


cur.execute("SELECT * FROM 'fare' LIMIT 10")

column_names = [desc[0] for desc in cur.description]

print(" | ".join(column_names))
print("-" * 80)

rows = cur.fetchall()
for row in rows:
    print(" | ".join(str(item) for item in row))

conn.close()

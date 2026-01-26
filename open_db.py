import sqlite3

conn = sqlite3.connect("kanpur_metro.db")
cur = conn.cursor()

print("\n--- ALL DATA (FIRST 10 ROWS) ---")
cur.execute("SELECT * FROM fare LIMIT 10")
cols = [d[0] for d in cur.description]
print(" | ".join(cols))
print("-" * 80)
for row in cur.fetchall():
    print(" | ".join(str(i) for i in row))

print("\n--- ALL STATIONS WITH CODES ---")
cur.execute("""
SELECT DISTINCT from_code, from_name
FROM fare
UNION
SELECT DISTINCT to_code, to_name
FROM fare
ORDER BY from_name
""")
print("CODE | STATION NAME")
print("-" * 50)
for row in cur.fetchall():
    print(f"{row[0]:4} | {row[1]}")

print("\n--- FARE BETWEEN TWO STATIONS ---")
from_station = "IIT KANPUR"
to_station = "KALYANPUR METRO"
cur.execute("""
SELECT from_name, to_name, weekday_fare, weekend_fare, stations_between
FROM fare
WHERE
(from_name = ? AND to_name = ?)
OR
(from_name = ? AND to_name = ?)
""", (from_station, to_station, to_station, from_station))
result = cur.fetchone()
if result:
    print(f"{result[0]} → {result[1]}: Rs {result[2]} (weekday), Rs {result[3]} (weekend), Stations between: {result[4]}")
else:
    print("No fare found for these stations")


conn.close()

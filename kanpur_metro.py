import requests
import sqlite3

STATIONS_API = "https://portal.upmetrorail.com/en/api/v2/stations_by_keyword/2/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

stations_raw = requests.get(STATIONS_API, headers=headers).json()

stations = []
for s in stations_raw:
    stations.append({
        "code": s["st_code"],
        "name": s["st_name"]
    })

print("Stations loaded:", len(stations))



conn = sqlite3.connect("kanpur_metro.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS fare (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_code TEXT,
    from_name TEXT,
    to_code TEXT,
    to_name TEXT,
    stations_between INTEGER,
    weekday_fare INTEGER,
    weekend_fare INTEGER
)
""")

conn.commit()
conn.close()

print("Database & table ready")



import time

fare_data = []

for src in stations:
    for dst in stations:
        if src["code"] == dst["code"]:
            continue

        url = f"https://portal.upmetrorail.com/en/api/v2/travel_distance_time_fare/2/{src['code']}/{dst['code']}/"

        try:
            res = requests.get(url, headers={
                "User-Agent": "Mozilla/5.0",
                "Referer": "https://portal.upmetrorail.com/"
            })

            data = res.json()

            fare_data.append({
                "from_code": src["code"],
                "from_name": data["from"],
                "to_code": dst["code"],
                "to_name": data["to"],
                "stations_between": data["stations"],
                "weekday_fare": data["weekday_fare"],
                "weekend_fare": data["weekend_fare"]
            })

            print(f"{src['code']} -> {dst['code']} = Rs {data['weekday_fare']}")

            time.sleep(0.4)

        except Exception as e:
            print("Error:", src["code"], dst["code"], e)

print("Total fares collected:", len(fare_data))



conn = sqlite3.connect("kanpur_metro.db")
cur = conn.cursor()

cur.executemany("""
INSERT INTO fare (
    from_code, from_name,
    to_code, to_name,
    stations_between,
    weekday_fare,
    weekend_fare
)
VALUES (
    :from_code, :from_name,
    :to_code, :to_name,
    :stations_between,
    :weekday_fare,
    :weekend_fare
)
""", fare_data)

conn.commit()
conn.close()

print("All fare data saved into database")

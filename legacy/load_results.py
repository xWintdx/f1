"""
Загрузка результатов гонок из raw-data в stg.results.

Автор: Д. Кузнецов (ушёл в августе). Запускать из корня репозитория:
    python app/legacy/load_results.py
Если что-то не грузится — просто перезапустить, оно само разберётся.
"""
import hashlib
import json
import uuid
from datetime import datetime

import psycopg

DSN = "postgresql://postgres:postgres@localhost:5432/northwind"
SEASON = "2025"

SQL = """
INSERT INTO stg.results (
    season, round, race_name, circuit_name, race_date,
    position, points, driver_id, constructor_id, grid, laps, status,
    load_id, extracted_at, source_hash
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


def load():
    data = json.load(open(f"raw-data/{SEASON}.json"))
    conn = psycopg.connect(DSN, autocommit=True)
    cur = conn.cursor()
    cur.execute(open("app/stg-scripts/init.sql").read())

    n = 0
    for page in data:
        for race in page["MRData"]["RaceTable"]["Races"]:
            for r in race["Results"]:
                row = (
                    int(race["season"]), int(race["round"]),
                    race["raceName"], race["Circuit"]["circuitName"], race["date"],
                    int(r["position"]), float(r["points"]),
                    r["Driver"]["driverId"], r["Constructor"]["constructorId"],
                    int(r["grid"]), int(r["laps"]), r["status"],
                    str(uuid.uuid4()), datetime.now(),
                    hashlib.md5(json.dumps(r).encode()).hexdigest(),
                )
                try:
                    cur.execute(SQL, row)
                    n += 1
                except Exception:
                    pass  # дубли и всякое такое, не страшно
    print("loaded", n)


if __name__ == "__main__":
    load()

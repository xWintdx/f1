def parse_season_data(season_races_results: list[dict]) -> list[dict]:
    race_results = []
    for results_by_page in season_races_results:
        races = (
            results_by_page.get("MRData")
            .get("RaceTable")
            .get("Races")
        )
        for race in races:
            current_season = race.get("season")
            season_round = race.get("round")
            race_name = race.get("raceName")
            circuit_name = race.get("Circuit").get("circuitName")
            race_date = race.get("date")
            race_time = race.get("time")
            for result in race.get("Results"):
                position = result.get("position")
                points = result.get("points")
                driver_id = result.get("Driver").get("driverId")
                constructor_id = result.get("Constructor").get("constructorId")
                grid = result.get("grid")
                laps = result.get("laps")
                status = result.get("status")
                race_results.append(
                    {
                        "season": current_season,
                        "season_round": season_round,
                        "race_name": race_name,
                        "circuit_name": circuit_name,
                        "race_date": race_date,
                        "race_time": race_time,
                        "position": position,
                        "points": points,
                        "driver_id": driver_id,
                        "constructor_id": constructor_id,
                        "grid": grid,
                        "laps": laps,
                        "status": status,
                    }
                )
    return race_results

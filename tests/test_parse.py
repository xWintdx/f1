import json
import pathlib

import pytest

from f1.parse import parse_season_data


@pytest.fixture
def get_season_data():
    file = pathlib.PurePath(__file__).parent / "fixtures" / "race_result.json"
    with open(file) as f:
        season_data = json.load(f)
    return season_data


def test_parse(get_season_data):
    points_by_places = {
        "1": "25",
        "2": "18",
        "3": "15",
        "4": "12",
        "5": "10",
        "6": "8",
        "7": "6",
        "8": "4",
        "9": "2",
        "10": "1",
        "11": "0",
        "12": "0",
        "13": "0",
        "14": "0",
        "15": "0",
        "16": "0",
        "17": "0",
        "18": "0",
        "19": "0",
        "20": "0",
    }

    test_season_data = parse_season_data(get_season_data)

    assert len(test_season_data) == 20
    assert {
        race.get("position"): race.get("points") for race in test_season_data
    } == points_by_places
    assert len(set([race.get("driver_id") for race in test_season_data])) == 20
    assert set(
        [race.get("status") for race in test_season_data if int(race.get("points")) > 0]
    ) == {"Finished"}
    assert set(
        [race.get("status") for race in test_season_data if int(race.get("points")) == 0]
    ) == {"Finished", "Retired"}

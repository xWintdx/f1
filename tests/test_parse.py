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
    assert parse_season_data(get_season_data)[0].get("points") == "25"

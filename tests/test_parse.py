import json

import pathlib

import pytest

from f1.parse import parse


@pytest.fixture
def data():
    file = pathlib.PurePath(__file__).parent / 'fixtures' / 'race_result.json'
    with open(file) as f:
        season_data = json.load(f)
    return season_data


def test_parse(data):
    assert parse(data)[0].get("points") == "25"

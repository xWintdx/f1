from src.f1.parse import parse
import pytest
import json

@pytest.fixture
def data():
    with open("D:\\f1\\tests\\fixtures\\race_result.json", "r") as f:
        season_data = json.load(f)
    return season_data

def test_parse(data):
    assert parse(data)[0].get("points") == '25'

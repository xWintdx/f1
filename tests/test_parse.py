import json
from pathlib import Path

import pytest

from f1.parse import parse


@pytest.fixture
def data():
    file = Path("/f1") / "tests" / "fixtures" / "race_result.json"
    with open(file) as f:
        season_data = json.load(f)
    return season_data


def test_parse(data):
    assert parse(data)[0].get("points") == "25"

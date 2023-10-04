from src.utils.from_json import from_json


def test_from_json():
    data = from_json()
    assert isinstance(data, list)

from src.utils.from_json import from_json


def test_from_json(monkeypatch, json_example):
    monkeypatch.setenv('src.utils.from_json', json_example)
    assert from_json(monkeypatch) == 1

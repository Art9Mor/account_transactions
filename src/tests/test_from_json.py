from sys import from_json

def test_from_json(mocker):
    mocker.patch('operations.json')
    assert from_json(mocker) == 1

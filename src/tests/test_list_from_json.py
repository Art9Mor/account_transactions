from <account_transactions>.utils.list_from_json import from_json

def test_from_json(mocker):
    mocker.patch('operations.json')
    assert from_json(mocker) == 1
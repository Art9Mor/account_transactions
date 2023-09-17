from src.utils.cleaned_data import cleaned_data


def test_cleaned_data(data_example):
    data = cleaned_data(data_example)

    assert len(data) == 2
    assert data[0]['id'] == 41428829
    assert data[1]['operationAmount']['amount'] == '9824.07'

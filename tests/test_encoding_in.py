from src.utils.encoding_in import encoding_in


def test_encoding_in(data_example):

    assert encoding_in(data_example[0]) == 'Счет **9589'
    assert encoding_in(data_example[2]) == 'Счет **6702'
    assert encoding_in(data_example[3]) == 'Счет **9781'

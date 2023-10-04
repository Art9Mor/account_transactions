from src.utils.encoding_out import encoding_out


def test_encoding_out(data_example):

    assert encoding_out(data_example[0]) == 'Maestro 1596 83** **** 5199'
    assert encoding_out(data_example[2]) == 'Счет 7510 68** **** 6952'
    assert encoding_out(data_example[3]) == 'Счет 7168 74** **** 5290'

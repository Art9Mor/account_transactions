from src.utils.last_values import last_values


def test_last_value(data_example):
    assert len(last_values(data_example, 3)) == 3
    assert len(last_values(data_example, 2)) == 2

from src.utils.operations_visor import operations_visor


def test_operations_visor(data_example):
    assert operations_visor(data_example[0]) == ('26.08.2019 Перевод организации\n'
                                                 'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                                                 '31957.58 руб.')
    assert operations_visor(data_example[2]) == ('30.06.2018 Перевод организации\n'
                                                 'Счет 7510 68** **** 6952 -> Счет **6702\n'
                                                 '9824.07 USD')

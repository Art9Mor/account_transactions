from src.utils.last_values import last_values


def test_last_value(data_example):
    assert last_values(data_example, 2) == [{'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
                                             'operationAmount': {'amount': '43318.34',
                                                                 'currency': {'name': 'руб.', 'code': 'RUB'}},
                                             'description': 'Перевод со счета на счет',
                                             'from': 'Счет 44812258784861134719',
                                             'to': 'Счет 74489636417521191160'},
                                            {'id': 27192367, 'state': 'CANCELED', 'date': '2018-12-24T20:16:18.819037',
                                             'operationAmount': {'amount': '991.49',
                                                                 'currency': {'name': 'руб.', 'code': 'RUB'}},
                                             'description': 'Перевод со счета на счет',
                                             'from': 'Счет 71687416928274675290',
                                             'to': 'Счет 87448526688763159781'}]

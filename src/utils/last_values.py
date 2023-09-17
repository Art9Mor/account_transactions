def last_values(data: list, get_values_number: int) -> list:
    """
    Receives data and returns a certain amount of it
    :param data: full list of operations
    :param get_values_number: number of operations to return
    :return: list of the last few transactions
    """
    data = sorted(data, key=lambda i: i['date'], reverse=True)
    data = data[:get_values_number]
    return data

def cleaned_data(data: list) -> list:
    """
    Make a list with operations with executed state
    :param data: list of dicts with operations
    :return: operations with executed state
    """
    data = [i for i in data if 'state' in i and i['state'] == 'EXECUTED']
    return data

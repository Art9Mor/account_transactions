def cleaned_data(data):
    data = [i for i in data if 'state' in i and i['state'] == 'EXECUTED']
    return data

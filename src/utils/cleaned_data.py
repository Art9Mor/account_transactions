def cleaned_data(data, empty_form=False):
    data = [i for i in data if 'state' in i and i['state'] == 'EXECUTED']
    return data

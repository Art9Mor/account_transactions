def last_values(data, get_values_number):
    data = sorted(data, key=lambda i: i['date'], reverse=True)
    data = data[:get_values_number]
    return data

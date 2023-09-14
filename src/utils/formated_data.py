from datetime import datetime


def formated_data(data, from_info):
    formated_data = []
    for i in data:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i['description']
        recipient = '**' + i['to'][::-5]
        amount = i['operationAmount']['amount']
        currency = i['operationAmount']['currency']['name']
        formated_data.append(f'''\
        {date} {description}
        {from_info} -> {recipient}
        {amount} {currency}''')
    return formated_data

from datetime import datetime


def formated_data(data):
    formated_data = []
    for i in data:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i['description']
        # from_info = i['from'][:4]
        from_bill = i['from'][::-6]
        recipient = '**' + i['to'][::-5]
        amount = i['operationAmount']['amount']
        currency = i['operationAmount']['currency']['name']
        formated_data.append(f'''\
        {date} {description}
        {from_bill} -> {recipient}
        {amount} {currency}''')
    return formated_data

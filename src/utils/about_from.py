def about_from(data):
    for element in data:
        source = element.get('from', 'Investor')
        if source != 'Investor':
            account_out = source.split()
            acc_out_num = account_out[-1]
            account_out[-1] = f'{acc_out_num[:4]} {acc_out_num[4:6]}** **** {acc_out_num[-4:]}'
            source = ' '.join(account_out)
            return source

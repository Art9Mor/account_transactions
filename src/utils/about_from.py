def about_from(data):
    for element in data:
        proto = element.get('from', 'Investor')
        if proto != 'Investor':
            account_out = proto.split()
            acc_out_num = account_out[-1]
            account_out[-1] = f'{acc_out_num[:4]} {acc_out_num[4:6]}** **** {acc_out_num[-4:]}'
            proto = ' '.join(account_out)
            return proto

def encoding_out(data: dict) -> str:
    """
    Encodes purpose account number into a required format
    """
    proto = data.get('from', 'Клиент')
    if proto != 'Клиент':
        account_out = proto.split()
        acc_out_num = account_out[-1]
        account_out[-1] = f'{acc_out_num[:4]} {acc_out_num[4:6]}** **** {acc_out_num[-4:]}'
        proto = ' '.join(account_out)
    return proto

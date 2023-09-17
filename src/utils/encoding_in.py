def encoding_in(data: dict) -> str:
    """
    Encodes source account number into a required format
    """
    account_params = data['to'].split()
    account_in = ' '.join(account_params[:-1])
    acc_num = account_params[-1]
    return f'{account_in} **{acc_num[-4:]}'

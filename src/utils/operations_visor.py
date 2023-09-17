from datetime import datetime
from src.utils.encoding_in import encoding_in
from src.utils.encoding_out import encoding_out


def operations_visor(data: dict) -> str:
    """
    Returns information about completed operations in a convenient form
    :param data:
    :return:
    """
    oper_date = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    description = data['description']
    amount = data['operationAmount']['amount']
    currency = data['operationAmount']['currency']['name']
    proto = encoding_out(data)
    purpose = encoding_in(data)
    return f'{oper_date} {description}\n{proto} -> {purpose}\n{amount} {currency}'

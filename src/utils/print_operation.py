from datetime import datetime
from src.utils.encoding_in import encoding_in
from src.utils.encoding_out import encoding_out


def print_operation(data: dict) -> str:
    """
    Returns operation information according to output required format
    """
    oper_date = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    description = data['description']
    amount = data['operationAmount']['amount']
    currency = data['operationAmount']['currency']['name']
    source = encoding_out(data)
    purpose = encoding_in(data)
    return f'{oper_date} {description}\n{source} -> {purpose}\n{amount} {currency}'

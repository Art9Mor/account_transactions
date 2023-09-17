import json
import os


def from_json() -> list:
    """
    Take json file and remake it in to the file we can work with
    :return: list of operations
    """
    current_dir = os.path.dirname(os.path.realpath(__file__))
    operations_file_path = os.path.join(current_dir, 'src/<account_transactions>/operations.json')

    with open(operations_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

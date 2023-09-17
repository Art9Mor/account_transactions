import json
import os


def from_json():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    operations_file_path = os.path.join(current_dir, "/home/artem/skypro/homeworks/done/course_work_3_/account_transactions/operations.json")
    with open(operations_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

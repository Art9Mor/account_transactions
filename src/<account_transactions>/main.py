from config import JSON_DATA, OPERATIONS_COUNT
from utils.from_json import from_json
from utils.cleaned_data import cleaned_data
from utils.last_values import last_values
from utils.formated_data import formated_data
from utils.about_form import about_from

def main():
    data = from_json(JSON_DATA)

    data = cleaned_data(data)
    data = last_values(data, OPERATIONS_COUNT)
    source = about_from(data)
    data = formated_data(data)

    for element in data:
        print(element, end='\n\n')


if __name__ == '__main__':
    main()

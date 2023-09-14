from config import JSON_DATA, OPERATIONS_COUNT
from src.utils.about_from import about_from
from src.utils.cleaned_data import cleaned_data
from src.utils.formated_data import formated_data
from src.utils.from_json import from_json
from src.utils.last_values import last_values


def main():

    data = from_json(JSON_DATA)

    data = cleaned_data(data)
    data = last_values(data, OPERATIONS_COUNT)
    from_info = about_from(data)
    data = formated_data(data, from_info)

    for element in data:
        print(element, end='\n\n')


if __name__ == '__main__':
    main()

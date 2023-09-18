from src.utils.cleaned_data import cleaned_data
from src.utils.from_json import from_json
from src.utils.last_values import last_values
from config import OPERATIONS_COUNT
from src.utils.operations_visor import operations_visor


def main():
    data = from_json()
    data = cleaned_data(data)
    data = last_values(data, OPERATIONS_COUNT)

    for element in data:
        print(operations_visor(element), end='\n\n')


if __name__ == '__main__':
    main()

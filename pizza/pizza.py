from sys import argv, exit
from csv import DictReader
from tabulate import tabulate


def main():
    correctly_used, message = is_usage_correct(argv)

    if not correctly_used:
        exit(message)

    filepath = argv[1]
    table = get_table(filepath)

    print(table)


def is_usage_correct(args):
    args_acceptable_length = 2
    args_length = len(args)

    if args_length < args_acceptable_length:
        return [False, 'Too few command-line arguments']

    if args_length > args_acceptable_length:
        return [False, 'Too many command-line arguments']

    filepath = args[1]

    if not filepath.lower().endswith('.csv'):
        return [False, 'Not a CSV file']

    try:
        with open(filepath, 'r') as _:
            pass
    except FileNotFoundError:
        return [False, 'File does not exist']

    return [True, 'Correctly used']


def get_table(filepath):
    table_data = list()

    with open(filepath, 'r') as file:
        reader = DictReader(file)

        for row in reader:
            table_data.append(row)

    return tabulate(table_data, headers='keys', tablefmt='grid')


if __name__ == '__main__':
    main()
from sys import argv, exit
from csv import DictReader, DictWriter


def main():
    used_correctly, message = is_usage_correct(argv)

    if not used_correctly:
        exit(message)

    input_filepath = argv[1]
    output_filepath = argv[2]
    convert_file_format(input_filepath, output_filepath)


def is_usage_correct(args):
    correct_args_length = 3
    args_length = len(args)

    if args_length < correct_args_length:
        return [False, 'Too few command-line arguments']

    if args_length > correct_args_length:
        return [False, 'Too many command-line arguments']

    input_filepath = args[1]
    output_filepath = args[2]

    if not input_filepath.lower().endswith('.csv'):
        return [False, f'{input_filepath} not a csv file']

    if not output_filepath.lower().endswith('.csv'):
        return [False, f'{output_filepath} not a csv file']

    try:
        with open(input_filepath, 'r') as _:
            pass
    except FileNotFoundError:
        return [False, f'Could not read {input_filepath}']

    return [True, 'Correctly used']


def convert_file_format(input, output):
    students = list()

    with open(input, 'r') as input_file:
        reader = DictReader(input_file)

        for row in reader:
            students.append(row)

    with open(output, 'w') as output_file:
        fieldnames = ['first', 'last', 'house']
        writer = DictWriter(output_file, fieldnames)

        writer.writeheader()
        for student in students:
            last, first = student['name'].split(', ')
            house = student['house']

            row = {'last': last, 'first': first, 'house': house}

            writer.writerow(row)


if __name__ == '__main__':
    main()

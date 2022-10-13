from sys import argv, exit


def main():
    continue_program_execution, message = is_usage_correct(argv)

    if not continue_program_execution:
        exit(message)

    filepath = argv[1]
    number_of_lines = count_lines(filepath)

    print(number_of_lines)


def is_usage_correct(argv):
    if len(argv) < 2:
        return [False, 'Too few command-line arguments']

    if len(argv) > 2:
        return [False, 'Too many command-line arguments']

    filepath = argv[1]

    if not filepath.lower().endswith('.py'):
        return [False, 'Not a python file']

    try:
        with open(filepath, 'r') as file:
            pass
    except FileNotFoundError:
        return [False, 'File does not exist']

    return [True, 'Used correctly']


def count_lines(filepath):
    count = 0

    with open(filepath, 'r') as file:
        for line in file:
            clean_line = line.strip()

            if clean_line.startswith('#') or len(clean_line) == 0:
                continue
            else:
                count += 1

    return count


if __name__ == '__main__':
    main()

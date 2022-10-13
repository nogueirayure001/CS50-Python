def main():
    names = get_names()

    say_farewell(names)


def get_names():
    names = list()

    finished_input = False
    while not finished_input:
        try:
            name = input('Name: ').strip()
            names.append(name)
        except EOFError:
            print()
            finished_input = True

    return names


def say_farewell(names):
    print(f'Adieu, adieu, to {names[0]}', end='')

    if len(names) > 2:
        for name in names[1:-1]:
            print(f', {name}', end='')
        print(f', and {names[-1]}', end='')

    elif len(names) == 2:
        print(f' and {names[-1]}', end='')

    print()


if __name__ == '__main__':
    main()

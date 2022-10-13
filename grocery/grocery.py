def main():
    groceries = get_groceries()
    display_groceries(groceries)


def get_groceries():
    groceries = {}

    not_finished = True
    while not_finished:
        try:
            item = input().lower().strip()
        except EOFError:
            print()
            not_finished = False
        else:
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1

    return groceries


def display_groceries(groceries):
    for item in sorted(list(groceries), key=str.upper):
        print(f'{groceries[item]} {item.upper()}')


if __name__ == '__main__':
    main()

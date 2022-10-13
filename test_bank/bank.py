def main():
    greeting = input('Say something: ').strip()

    print(f'${value(greeting)}')


def value(greeting):
    greetingClean = greeting.lower()

    if greetingClean.startswith('hello'):
        return 0
    elif greetingClean.startswith('h'):
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()

def convert(str):
    return str.replace(':)', '\U0001F642').replace(':(', '\U0001F641')


def main():
    str = input('Say something: ')
    new_str = convert(str)
    print(new_str)


main()

def main():
    str = input('Say something: ').lower().strip()

    if str.startswith('hello'):
        print('$0')
    elif str.startswith('h'):
        print('$20')
    else:
        print('$100')


main()

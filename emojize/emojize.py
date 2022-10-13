import emoji


def main():
    user_input = input('Input: ')
    output = convert_code_to_emoji(user_input)

    print(f'Output: {output}')


def convert_code_to_emoji(string):
    return emoji.emojize(string, language='alias')


if __name__ == '__main__':
    main()

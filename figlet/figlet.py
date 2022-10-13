from sys import argv, exit
from pyfiglet import Figlet, FontNotFound


def main():
    check_correct_usage()

    convert_user_input()


def check_correct_usage():
    used_with_args = len(argv) == 3
    used_without_args = len(argv) == 1

    if used_with_args:
        flag = argv[1]
        if flag not in ['-f', '--font']:
            exit('Invalid usage')
    elif not used_without_args:
        exit('Invalid usage')


def convert_user_input():
    selected_font = argv[2] if len(argv) == 3 else ''

    if selected_font == '':
        figlet_converter = Figlet()
    else:
        try:
            figlet_converter = Figlet(font=selected_font)
        except FontNotFound:
            exit('Invalid usage')

    user_input = input('Input: ')

    output = figlet_converter.renderText(user_input)

    print(output)


if __name__ == '__main__':
    main()

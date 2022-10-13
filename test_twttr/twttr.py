def main():
    str = input('Input: ')
    shortened_str = shorten(str)
    print('Output:', shortened_str)


def shorten(str):
    str_letters = list()

    for letter in str:
        if not isvowel(letter):
            str_letters.append(letter)

    return ''.join(str_letters)


def isvowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if letter.lower() in vowels:
        return True

    return False


if __name__ == '__main__':
    main()

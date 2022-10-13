def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not starts_with_two_letters(s):
        return False

    if not has_max_six_letters(s):
        return False

    if has_number_in_middle(s):
        return False

    if fist_number_is_zero(s):
        return False

    if not s.isalnum():
        return False

    return True


def starts_with_two_letters(string):
    if not (len(string) >= 2 and string[0].isalpha() and string[1].isalpha):
        return False

    return True


def has_max_six_letters(string):
    return len(string) <= 6


def has_number_in_middle(string):
    has_number = False

    for letter in string:
        if letter.isdigit():
            has_number = True

        if has_number and letter.isalpha():
            return True

    return False


def fist_number_is_zero(string):
    for letter in string:
        if letter.isdigit():
            if letter == '0':
                return True
            else:
                return False

    return False


main()

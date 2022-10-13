def main():
    fraction = get_fraction("Fraction: ")
    show_result(fraction)


def get_fraction(prompt):
    valid_input = False

    while not valid_input:
        try:
            a, b = input(prompt).split("/")

            if str.isdecimal(a) and str.isdecimal(b) and int(a) <= int(b):
                valid_input = True
            else:
                pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

    return round(100 * float(a) / float(b))


def show_result(fraction):
    if fraction >= 99:
      print("F")
    elif fraction > 1:
      print(f"{fraction}%")
    else:
      print("E")


main()

def main():
    fraction = input("Fraction: ")

    try:
        percent = convert(fraction)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        print(gauge(percent))


def convert(fraction):
    a, b = fraction.split("/")

    if int(a) > int(b) and int(b) != 0:
        raise ValueError

    return round(100 * float(a) / float(b))


def gauge(percent):
    if percent >= 99:
        return "F"
    elif percent > 1:
        return f"{percent}%"
    else:
        return "E"


if __name__ == '__main__':
    main()

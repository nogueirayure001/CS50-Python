import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    num_of_groups = 4

    match = re.match(
        r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$', ip)

    if not match:
        return False

    for i in range(1, num_of_groups):
        if not (match.group(i) and 0 <= int(match.group(i)) <= 255):
            return False

    return True


if __name__ == "__main__":
    main()


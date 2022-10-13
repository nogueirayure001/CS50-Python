import re


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(
        r'([\s]um[\s,.]*|^um[\s,.]*|[\s]um[.!?]*$|^um[.!?]*$)', s, flags=re.IGNORECASE)

    return len(matches)


if __name__ == "__main__":
    main()

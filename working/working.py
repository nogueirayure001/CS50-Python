import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.match(
        '([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM) to ([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM)', s)

    if not match:
        raise ValueError

    starting_hour = int(match.group(1))
    starting_minute = 0 if match.group(2) == None else int(match.group(2))
    starting_period = match.group(3)
    starting_hour, starting_minute = translate_to_24h_format(
        starting_hour, starting_minute, starting_period)

    finishing_hour = int(match.group(4))
    finishing_minute = 0 if match.group(5) == None else int(match.group(5))
    finishing_period = match.group(6)
    finishing_hour, finishing_minute = translate_to_24h_format(
        finishing_hour, finishing_minute, finishing_period)

    return f'{starting_hour:02}:{starting_minute:02} to {finishing_hour:02}:{finishing_minute:02}'


def translate_to_24h_format(hour, minute, period):
    translated_hour = hour
    translated_minute = minute

    if period == 'AM':
        if translated_hour == 12:
            translated_hour = 0
    else:
        if not translated_hour == 12:
            translated_hour += 12

    return [translated_hour, translated_minute]


if __name__ == "__main__":
    main()

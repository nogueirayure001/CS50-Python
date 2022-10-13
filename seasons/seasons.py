import re
import sys
from datetime import date
import inflect

p = inflect.engine()


def main():
    birthdate_string = input('Date of Birth: ')

    birthdate = convert_to_date(birthdate_string)

    if not birthdate:
        sys.exit('Invalid date')

    minutes = get_minutes_since_birth(birthdate)

    print(minutes)


def convert_to_date(date_string):
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date_string)

    if not match:
        print('aqui 1')
        return None

    year = int(match.group(1))
    month = int(match.group(2))
    day = int(match.group(3))

    try:
        converted_date = date(year, month, day)
    except ValueError:
        return None

    return converted_date


def get_minutes_since_birth(birthdate):
    seconds_since = (date.today() - birthdate).total_seconds()

    minutes_since = round(seconds_since / 60)

    minutes_since_words = p.number_to_words(minutes_since).replace(' and ', ' ').capitalize()

    return f'{minutes_since_words} minutes'


if __name__ == "__main__":
    main()

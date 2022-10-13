MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    valid_input = False

    while not valid_input:
        date = get_date()

        if is_month_day_year_formatted(date):
            display_M_D_Y_in_ISO(date)
            valid_input = True

        elif is_month_name_day_year_formatted(date):
            display_M_NAME_D_Y_in_ISO(date)
            valid_input = True


def get_date():
    date = input('Date: ').strip().title()
    return date


def is_month_day_year_formatted(date):
    date_pieces = date.split('/')

    if not len(date_pieces) == 3:
        return False

    try:
        if not 1 <= int(date_pieces[0]) <= 12:
            return False

        if not 1 <= int(date_pieces[1]) <= 31:
            return False

        if not int(date_pieces[2]) >= 1:
            return False
    except ValueError:
        return False

    return True


def is_month_name_day_year_formatted(date):
    date_pieces = date.split()

    if not len(date_pieces) == 3:
        return False

    if date_pieces[0] not in MONTHS:
        return False

    day = date_pieces[1].split(',')
    if not len(day) == 2:
        return False

    try:
        day = int(day[0])
    except ValueError:
        return False

    if not 1 <= day <= 31:
        return False

    try:
        if not int(date_pieces[2]) >= 1:
            return False
    except ValueError:
        return False

    return True


def display_M_D_Y_in_ISO(date):
    [month, day, year] = date.split('/')
    print(f'{year}-{int(month):02}-{int(day):02}')


def display_M_NAME_D_Y_in_ISO(date):
    [month, day, year] = date.split()
    month = MONTHS.index(month) + 1
    day = day.split(',')[0]

    print(f'{year}-{int(month):02}-{int(day):02}')


if __name__ == '__main__':
    main()

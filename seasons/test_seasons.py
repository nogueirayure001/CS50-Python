from datetime import date
from seasons import get_minutes_since_birth, convert_to_date


def test_one_year_ago():
    today = date.today()
    one_year_ago = date(today.year - 1, today.month, today.day)

    assert get_minutes_since_birth(
        one_year_ago) == 'Five hundred twenty-five thousand, six hundred minutes'


def test_two_years_ago():
    today = date.today()
    two_years_ago = date(today.year - 2, today.month, today.day)

    assert get_minutes_since_birth(
        two_years_ago) == 'One million, fifty-one thousand, two hundred minutes'


def test_invalid_birthdate():
    invalid_dates = ['1993/06/06', '2000-33-44']

    for invalid_date in invalid_dates:
        assert convert_to_date(invalid_date) == None

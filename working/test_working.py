import pytest
from working import convert


def test_working_no_minutes():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'


def test_working_minutes():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'
    assert convert('12:15 AM to 12:30 PM') == '00:15 to 12:30'
    assert convert('9:55 AM to 1:00 PM') == '09:55 to 13:00'


def test_working_inverted_period():
    assert convert('9 PM to 5 AM') == '21:00 to 05:00'
    assert convert('12:00 PM to 12:00 AM') == '12:00 to 00:00'


def test_working_wrong_input():
    with pytest.raises(ValueError):
        assert convert('9 AM5 PM')
    with pytest.raises(ValueError):
        assert convert('12:60 AM to 12:55 PM')
    with pytest.raises(ValueError):
        assert convert('33:60 AM to 12:55 PM')
    with pytest.raises(ValueError):
        assert convert('12:55 AM - 12:55 PM')
    with pytest.raises(ValueError):
        assert convert(' to ')

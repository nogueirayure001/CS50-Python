import pytest
from fuel import convert, gauge


def test_convert_pass():
    assert convert('1/100') == 1
    assert convert('5/10') == 50
    assert convert('3/9') == 33
    assert convert('7/9') == 78


def test_convert_fail():
    with pytest.raises(ZeroDivisionError):
        convert('5/0')

    with pytest.raises(ValueError):
        convert('cat/5')

    with pytest.raises(ValueError):
        convert('10/5')

def test_gauge():
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(2) == '2%'

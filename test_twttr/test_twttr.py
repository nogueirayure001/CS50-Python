from twttr import shorten

def test_shorten_lowercase():
    assert shorten('twitter') == 'twttr'
    assert shorten('hello, world') == 'hll, wrld'


def test_shorten_uppercase():
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('HELLO, WORLD') == 'HLL, WRLD'

def test_shorten_scrambled():
    assert shorten('0TwIItTer&*') == '0TwtTr&*'

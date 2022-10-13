from numb3rs import validate

def test_valid_ips():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True

def test_invalid_ips():
    assert validate('cat') == False
    assert validate('55.0.0.1000') == False
    assert validate('127.0.0.1.9') == False
    assert validate('55.555.4.3') == False
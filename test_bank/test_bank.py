from bank import value

def test_value_lowercase():
  assert value('hello') == 0
  assert value('hi there') == 20
  assert value('whats up') == 100

def test_value_uppercase():
  assert value('Hello') == 0
  assert value('Hi there') == 20
  assert value('Whats up') == 100

def test_value_nonletters():
  assert value('.63gf') == 100
  assert value('&&&&323v') == 100
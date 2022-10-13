from plates import is_valid

def test_plates_rule1():
  assert is_valid('AE22') == True
  assert is_valid('A22') == False

def test_plates_rule2():
  assert is_valid('A') == False
  assert is_valid('bb') == True
  assert is_valid('AE2222') == True
  assert is_valid('AE22222') == False

def test_plates_rule3():
  assert is_valid('AAA222') == True
  assert is_valid('AAA22A') == False
  assert is_valid('AAA02') == False
  assert is_valid('AAA20') == True

def test_plates_rule4():
  assert is_valid('!AA22') == False
  assert is_valid('AAA!22') == False
  assert is_valid('AAA22!') == False
  assert is_valid(' AA22') == False
  assert is_valid('AAA 22') == False
  assert is_valid('AAA22 ') == False
  assert is_valid('$AA22') == False
  assert is_valid('AAA$22') == False
  assert is_valid('AAA22$') == False
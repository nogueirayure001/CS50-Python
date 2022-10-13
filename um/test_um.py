from um import count

def test_um_beginning():
  assert count('um') == 1
  assert count('um, hello..') == 1
  assert count('ummy') == 0

def test_um_ending():
  assert count('thats, um') == 1
  assert count('thats, Um...') == 1
  assert count('Um') == 1
  assert count('and, ummy') == 0

def test_um_between():
  assert count('hello, um, world') == 1
  assert count('that\'s Um... cs50') == 1
  assert count('Um, thanks, um, i guess') == 2
  assert count('Um? Mum? this album is, um, umm.. ') == 2
import pytest
from lines import is_usage_correct, count_lines

usage_tester_values = {
    "tooFew": [False, 'Too few command-line arguments'],
    "tooMany": [False, 'Too many command-line arguments'],
    "nonExisting": [False, 'File does not exist'],
    "notPython": [False, 'Not a python file'],
    "correct": [True, 'Used correctly']
}

base_path = 'test_lines/test_files'


def test_number_of_args():
    assert is_usage_correct(['lines.py']) == usage_tester_values["tooFew"]
    assert is_usage_correct(['lines.py', f'{base_path}/existing.py', 'extra.txt']
                            ) == usage_tester_values["tooMany"]
    assert is_usage_correct(['lines.py', f'{base_path}/nonexisting.py']
                            ) == usage_tester_values["nonExisting"]
    assert is_usage_correct(['lines.py', f'{base_path}/nonpython.txt']
                            ) == usage_tester_values["notPython"]
    assert is_usage_correct(['lines.py', f'{base_path}/filled.py']
                            ) == usage_tester_values["correct"]

def test_counting():
    assert count_lines(f'{base_path}/filled.py') == 6
    assert count_lines(f'{base_path}/filled2.py') == 8
    assert count_lines(f'{base_path}/existing.py') == 0
from lib.report_length import *

def test_four_characters():
    result = report_length("four")
    assert result == "This string was 4 characters long"

def test_three_characters():
    result = report_length("aaa")
    assert result == "This string was 3 characters long"

def test_zero_characters_long():
    result = report_length("")
    assert result == "This string was 0 characters long"
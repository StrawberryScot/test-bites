from lib.codeword import *

def test_with_incorrect_codeword():
    result = check_codeword("abcd")
    assert result == "WRONG!"

def test_with_close_codeword():
    result = check_codeword("haste")
    assert result == "Close, but nope."

def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

from lib.string_builder import *

def test_initial_output_is_empty_string():
    test_string = StringBuilder()
    result = test_string.output()
    assert result == ""

def test_initial_size_is_zero():
    test_string = StringBuilder()
    result = test_string.size()
    assert result == 0

def test_add_word():
    test_string = StringBuilder()
    test_string.add("Word")
    test_string.add("Word")
    result = test_string.output()
    assert result == "WordWord"
from lib.greet import *

def test_returns_name():
    result = greet("Ben")
    assert result == "Hello, Ben!"
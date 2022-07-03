from fuel import convert
from fuel import gauge
from pytest import raises

def test_convert_positive():
    assert convert("0/9") == 0
    assert convert("1/2") == 50


def test_convert_errors():
#sadly had to look up how to check if an error was raised. Before I was trying to assert an error was returned.
#I wanted to test for negative values, but check50 doesn't like that.
    with raises(ValueError):
        convert("2/1")
    with raises(ValueError):
        convert("cat/21")
    with raises(ZeroDivisionError):
        convert("21/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

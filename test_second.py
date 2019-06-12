import pytest

def f():
   raise SystemExit(1)

def add(a , b):
    return a+b

def sum():
    assert add(2,2)==5


def test_mytest():
    with pytest.raises(SystemExit):
      f()
from factorial_module.factorial_module import *

# the factorial_iterative test:

def test_factorial_iterative():
    actual = factorial_iterative(5)
    expected = 120
    assert actual == expected

def test_factorial_iterative():
    actual = factorial_iterative(7)
    expected = 5040
    assert actual == expected

def test_factorial_iterative():
    actual = factorial_iterative(3)
    expected = 6
    assert actual == expected        

# the factorial_recursive test:

def test_factorial_recursive():
    actual = factorial_recursive(4)
    expected =24
    assert actual == expected    

def test_factorial_recursive():
    actual = factorial_recursive(1)
    expected = 1
    assert actual == expected    

def test_factorial_recursive():
    actual = factorial_recursive(3)
    expected =6
    assert actual == expected    

# clumsy function test:

def test_clumsy():
    actual = clumsy(6)
    expected = 8
    assert actual == expected    

def test_clumsy():
    actual = clumsy(4)
    expected = 7
    assert actual == expected  

def test_clumsy():
    actual = clumsy(2)
    expected = 2
    assert actual == expected      

def test_clumsy():
    actual = clumsy(5)
    expected = 7
    assert actual == expected  

def test_clumsy():
    actual = clumsy(3)
    expected = 6
    assert actual == expected          
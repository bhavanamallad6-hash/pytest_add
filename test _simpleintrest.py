from simple_interest import simple_interest

def test_simple_interest():
    assert simple_interest(5000, 10, 2) == 1000

def test_simple_interest2():
    assert simple_interest(1000, 5, 3) == 150

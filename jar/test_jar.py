import pytest
from jar import Jar


def test_capacity():
    jar1 = Jar()
    assert jar1.capacity == 12

    jar2 = Jar(20)
    assert jar2.capacity == 20

    with pytest.raises(ValueError):
        Jar(-5)


def test_size():
    jar1 = Jar()
    assert jar1.size == 0

    jar1.size = 7
    assert jar1.size == 7

    with pytest.raises(ValueError):
        Jar(-5)


def test_deposit():
    jar1 = Jar(20)

    jar1.deposit(5)
    assert jar1.size == 5

    jar1.deposit(5)
    assert jar1.size == 10

    jar1.deposit(0)
    assert jar1.size == 10

    with pytest.raises(ValueError):
        jar1.deposit(50)

    with pytest.raises(ValueError):
        jar1.deposit(-1)


def test_withdraw():
    jar1 = Jar(20)
    jar1.deposit(15)

    jar1.withdraw(5)
    assert jar1.size == 10

    jar1.withdraw(3)
    assert jar1.size == 7

    with pytest.raises(ValueError):
        jar1.withdraw(8)

    with pytest.raises(ValueError):
        jar1.withdraw(-1)


def test_str():
    jar1 = Jar(20)

    jar1.deposit(12)

    assert jar1.__str__() == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'

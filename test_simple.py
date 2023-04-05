import pytest


@pytest.fixture
def user(browser_name):
    print('\nСоздаём User ID')
    yield 123 # после yield выполняется код, который будет запущен после теста
    print('\nТеперь удаляем User ID')


def test_addition(user, browser_name):
    print('test1')
    assert browser_name == "Chrome"
    assert user == 123
    a = 1 + 2
    assert a == 3


def test_addition2(user, browser_name):
    print('test2')

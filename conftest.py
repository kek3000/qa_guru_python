import pytest


# все общие фикстуры мы пишем в файле conftest.py, они будут видны всем тестовым классам по умолчанию
@pytest.fixture(scope="session")
def browser_name():
    print('Я выполняюсь 1 раз')
    return "Chrome"

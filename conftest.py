import pytest
from selene import be
from selene.support.shared import browser


# все общие фикстуры мы пишем в файле conftest.py, они будут видны всем тестовым классам по умолчанию

@pytest.fixture(scope="session")  # браузер не будет закрываться между тестами
def browser_start():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    browser.open('https://www.google.com')
    yield
    print('Тесты закончены')

from selene.support.shared import browser
from selene import be, have


def test1(browser_start):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    print('\nтест0 пройден')


def test2():
    browser.element('[name="q"]').clear().type('1273887yhfksdajhf781yfds$%^&*(').press_enter()
    browser.element('#result-stats').should(have.text('примерно 0'))
    print('\nтест1 пройден')

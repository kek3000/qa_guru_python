from selene.support.shared import browser
from selene import be, have
import os

# browser.open('https://google.com')
# browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

browser.open('https://demoqa.com/automation-practice-form')

#Name
browser.element('#firstName').type('Nikita')
browser.element('#lastName').type('Alekseev')

#Email
browser.element('#userEmail').type('test@test.ru')

#Gender
browser.element('#gender-radio-1').double_click()

#Mobile(10 Digits)
browser.element('#userNumber').type('79999999999')

#Date of Birth
browser.element('#dateOfBirthInput').press()
browser.element('.react-datepicker__month-select').click()
browser.element('option[value="6"]').click()
browser.element('.react-datepicker__year-select').click()
browser.element('option[value="1991"]').click()
browser.element('div[aria-label="Choose Thursday, July 18th, 1991"]').click()

#Subjects
browser.execute_script("document.querySelector('.subjects-auto-complete__value-container').innerHTML = 'Automation QA'")

#Hobbies
browser.element('label[for="hobbies-checkbox-1"]').click()
browser.element('label[for="hobbies-checkbox-3"]').click()

#Picture
browser.element('#uploadPicture').send_keys(os.getcwd()+"/image.jpg")

#Current Address
browser.element('#currentAddress').type('Russia, Reutov')

#State and City - не смог одолеть..
# browser.element('#state').click().select_by_value(2)
# browser.element('//*[@id="state"]').send_keys('NCR')
# browser.element('//*[@id="state"]/div/div[1]/div[1]').press()
# browser.element('#state').select_by_visible_text('Haryana')

#Submit
browser.element('#submit').click()


import time

from behave import *

from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import allure

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

@then('go screenshot for allure "{name}"')
def step_impl(context, name):
    allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)


@given('open site "{url}"')
def step_impl(context, url):
    context.driver.get(url)


@then('enter data in the field username "{user}" By.ID "{locator}"')
def step_impl(context, user, locator):
    context.driver.find_element(By.ID, locator).send_keys(user)


@then('enter data in the username login "{password}" By.XPATH "{locator}"')
def step_impl(context, password, locator):
    context.driver.find_element(By.XPATH, locator).send_keys(password)


@step('press the button for Login to enter the admin panel By.XPATH "{locator}"')
def step_impl(context, locator):
    context.driver.find_element(By.XPATH, locator).click()


@then('checking a successful login to the admin page, By.XPATH "{locator}"')
def step_impl(context, locator):
    result = context.driver.find_element(By.XPATH, locator).text
    assert result == "Django administration", 'Administrator logged in not successfully'


@given('click button create user By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()


@then('enter data in the username By.XPATH "{locator}" send keys "{name}"')
def step_impl(context, locator, name):
    context.driver.find_element(By.XPATH, locator).send_keys(name)


@step('enter data in the password By.XPATH "{locator}" send keys "{password}"')
def step_impl(context, locator, password):
    context.driver.find_element(By.XPATH, locator).send_keys(password)


@step('enter data in the password confirm By.XPATH "{locator}" send keys "{password}"')
def step_impl(context, locator, password):
    context.driver.find_element(By.XPATH, locator).send_keys(password)


@step('click button save new user By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()


@then('checking a successful create new user, By.XPATH "{locator}"')
def step_impl(context, locator):
    result = context.driver.find_element(By.XPATH, locator).text
    assert result == 'The user “Popravka” was added successfully. You may edit it ' \
                                                     'again below.', 'New user is not create'


@given('click button users,go to the user page By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()


@then('in the search box By.XPATH "{locator}" send data "{name}"')
def step_impl(context, locator, name):
    context.driver.find_element(By.XPATH, locator).send_keys(name)


@then('click button Search By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()

@then('checking a successful find new user, By.XPATH "{locator}"')
def step_impl(context, locator):
    result = context.driver.find_element(By.XPATH, locator).text
    assert result == "Popravka", "New user is not find"


@step('click on user  and go to the user page to edit it By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()


@then('update user data in the field first name By.XPATH "{locator}" send keys "{first_name}"')
def step_impl(context, locator, first_name):
    context.driver.find_element(By.XPATH, locator).send_keys(first_name)



@step('update user data in the field last name By.XPATH "{locator}" send keys "{last_name}"')
def step_impl(context, locator, last_name):
    context.driver.find_element(By.XPATH, locator).send_keys(last_name)


@step('update user data in the field email By.XPATH "{locator}" send keys "{email}"')
def step_impl(context, locator, email):
    context.driver.find_element(By.XPATH, locator).send_keys(email)


@step('change staff status By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()
    time.sleep(3)


@step('click the button to save the result By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()


@given('check update user data in the field first name By.XPATH "{locator}" keys "{first_name}"')
def step_impl(context, locator, first_name):
    result = context.driver.find_element(By.XPATH, locator).get_attribute("value")
    assert result == first_name, " first name does not match"



@step('check update user data in the field last name By.XPATH "{locator}" keys "{last_name}"')
def step_impl(context, locator, last_name):
    result = context.driver.find_element(By.XPATH, locator).get_attribute("value")
    assert result == last_name, " last name does not match"



@step('check update user data in the field email By.XPATH "{locator}" keys "{email}"')
def step_impl(context, locator, email):
    result = context.driver.find_element(By.XPATH, locator).get_attribute("value")
    assert result == email, " email name does not match"


@step('check staff status true By.XPATH "{locator}" keys "{true}"')
def step_impl(context, locator, true):
    result = context.driver.find_element(By.XPATH, locator).get_attribute("checked")
    assert result == true, " staff status does not match"


@step('tick the user you want to delete By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()



@step('click on the drop down list to select By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()



@step('click on the drop down list to select options delete By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()


@step('click button GO to confirm deletion By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()



@then('click button YES I AM SURE By.XPATH "{button}"')
def step_impl(context, button):
    context.driver.find_element(By.XPATH, button).click()

@then('check delete user By.XPATH "{locator}" result: "{text_result}"')
def step_impl(context, locator, text_result):
    result = context.driver.find_element(By.XPATH, locator).text
    assert result == text_result, 'New user is not delete'

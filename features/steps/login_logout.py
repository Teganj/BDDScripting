from behave import *
from selenium.webdriver import ActionChains

from functions.webdriver import *
from variables.variables import *

use_step_matcher("re")


@when("user navigates to (?P<URL>.+)")
def navigate_to_url(context, URL):
    context.browser.get(URL)


@step("can see the (?P<text>.+)")
def assert_landing(context, text):
    landing_text = by_xpath(context, '/html/body/div/div[1]/h1').text
    try:
        assert landing_text == text
    except AssertionError as e:
        print('Landing assertion FAIL')
        screenshot_to_report(context, screenshot_location)
        assert landing_text == text


@step(
    "user can type (?P<username>.+) and (?P<password>.+) and click login button")
def login(context, username, password):
    username_field = by_id(context, 'id_username')
    username_field.clear()
    username_field.send_keys(username)

    password_field = by_id(context, 'id_password')
    password_field.clear()
    password_field.send_keys(password)

    signin_button = by_name(context, 'button')
    signin_button.click()


@step("user can see text (?P<login_message>.+)")
def assert_login(context, login_message):
    profile = by_class(context, 'rbtn--primary').text
    try:
        assert profile == login_message
    except AssertionError as e:
        print('Assertion FAIL')
        screenshot_to_report(context, screenshot_location)
        assert profile == login_message


@step("user click logout")
def logout(context):
    action = ActionChains(context.browser)
    first_level_menu = by_class(context, 'rbtn--primary')
    action.move_to_element(first_level_menu).perform()
    second_level_menu = by_id(context, 'e2e__3')
    action.move_to_element(second_level_menu).perform()
    second_level_menu.click()


@step("user can see (?P<logout_message>.+)")
def assert_logout(context, logout_message):
    out_text = by_xpath(context, '//*[@id="rightcontainer"]/div/div/a').text
    try:
        assert out_text == logout_message
    except AssertionError as e:
        print('Logout Assertion FAIL')
        screenshot_to_report(context, screenshot_location)
        assert out_text == logout_message

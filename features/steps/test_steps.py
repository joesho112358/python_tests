from behave import *
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from pages.google.home_page import HomePage as google_home
from pages.python.home_page import HomePage as python_home
from pages.google.result_page import ResultPage as google_result


@given('I am on Google')
def step_impl(context):
	driver = context.driver
	home = google_home(driver)
	home.get("https://www.google.com")
	assert "Google" == driver.title

@given('I have searched for python')
def step_impl(context):
	context.execute_steps("""
        given I am on Google
        when I search for "python"
    """)

@when('I search for "{text}"')
def step_impl(context, text):
	home = google_home(context.driver)
	home.search_element = text
	home.search_element = Keys.RETURN

@then('I can see a python download link')
def step_impl(context):
	driver = context.driver
	driver.implicitly_wait(10)
	result = google_result(driver)
	assert result.python_download_link.is_displayed

@when('I click the python link')
def step_impl(context):
	driver = context.driver
	result = google_result(driver)
	driver.implicitly_wait(10)
	result.python_download_link.click()

@then('I am on the python home page')
def step_impl(context):
	driver = context.driver
	driver.implicitly_wait(10)
	home = python_home(driver)
	assert home.python_logo.is_displayed
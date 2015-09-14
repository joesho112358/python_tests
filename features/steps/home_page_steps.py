from behave import *
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from pages.python.home_page import HomePage as python_home
from pages.python.result_page import ResultPage as python_result


@given('I am on the Python main page')
def step_impl(context):
	driver = context.driver
	home = python_home(driver)
	home.get(home.url)
	assert "Welcome to Python.org" == driver.title
	
@when('I search for "{text}"')
def step_impl(context, text):
	home = python_home(context.driver)
	home.search = 'python'
	home.search_submit.click()
	
@then('I am on the python results page')
def step_impl(context):
	result = python_result(context.driver)
	assert result.content_header.text == 'Search Python.org'
	
	
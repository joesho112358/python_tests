from behave import *
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from pages import home_page
from pages import result_page

@given('I am on Google')
def step_impl(context):
	driver = context.driver
	home = home_page.HomePage(driver)
	home.get("https://www.google.com")
	assert "Google" == driver.title

@when('I serach for "{text}"')
def step_impl(context, text):
	home = home_page.HomePage(context.driver)
	home.search_element = text
	home.search_element = Keys.RETURN

@then('I can see a tutorial\'s point link')
def step_impl(context):
	driver = context.driver
	driver.implicitly_wait(10)
	assert "No results found." not in driver.page_source
	result = result_page.ResultPage(driver)
	assert "Tutorialspoint" in result.search_result_table_element.text
	assert "Python" in result.search_result_table_element.text
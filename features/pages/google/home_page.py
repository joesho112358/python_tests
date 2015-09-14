from page_objects import PageObject, PageElement

class HomePage(PageObject):

	url = "https://www.google.com"

	search_element = PageElement(name='q')



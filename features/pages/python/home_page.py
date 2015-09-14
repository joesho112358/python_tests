from page_objects import PageObject, PageElement

class HomePage(PageObject):

	url = "https://www.python.org"

	python_logo = PageElement(class_name='python-logo')
	
	search = PageElement(id_='id-search-field')
	search_submit = PageElement(class_name='search-button')



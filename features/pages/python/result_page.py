from page_objects import PageObject, PageElement

class ResultPage(PageObject):

	content_section = PageElement(class_name='main-content ')
	content_header = PageElement(tag_name='h2')




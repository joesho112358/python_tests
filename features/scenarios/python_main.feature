Feature: Main Python page

  Scenario: 1 I can search on the page
    Given I am on the Python main page
    When I search for "python"
    Then I am on the python results page
	
	
Feature: I can search for Python

  Scenario: 1 I can search for Python
    Given I am on Google
    When I search for "python"
    Then I can see a python download link

  Scenario: 2 I can access the Python homepage through Google
    Given I have searched for python
    When I click the python link
    Then I am on the python home page
Feature: I can search for Python

  Scenario: 1 I can search for Python
    Given I am on Google
    When I search for "python"
    Then I can see a python download link
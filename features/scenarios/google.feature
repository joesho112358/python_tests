Feature: I can search for Python tutorials

  Scenario: 1 I can search for Python
    Given I am on Google
    When I serach for "python"
    Then I can see a tutorial's point link
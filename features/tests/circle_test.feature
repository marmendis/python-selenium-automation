Feature: Verify Target Circle benefits
  As a Target customer
  I want to see all Target Circle benefits
  So that I can be aware of them

  Scenario: Verify there are at least 10 benefit cells on the Target Circle page
    Given I open the Target Circle page
    Then I should see at least 10 benefit cells

Feature: test if my target cart is empty


  Scenario: Verify empty cart message
    Given open Target main page
    When I click on the cart icon
    Then verify the message Your cart is empty

    Scenario: Sign in account
    Given open Target main page
    When I click sign
    When I click sign from navigation menu
    Then verify sign in form opened
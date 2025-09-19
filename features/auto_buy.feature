Feature: Add product to cart
  As a Target customer
  I want to add a product to the cart
  So that I can verify it is added

  Scenario: Add a product to the cart and verify
    Given open the Target homepage
    When search for "toothpaste"
    When select the first product
    When add the product to the cart
    Then I should see items in the cart with subtotal

Feature: Checkout
  Scenario: Complete checkout with items in the cart
    Given I am logged in to SauceDemo
    And I have items in my cart
    When I checkout with first name "Test_Firstname", last name "Test_lastname", and zip code "E1A353"
    Then I should see the order confirmation "Thank you for your order!"

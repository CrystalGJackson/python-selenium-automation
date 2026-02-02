Feature: Tests for search

#
#  Scenario: User can search for a tea on Target
#    Given Open Target main page
#    When Search for tea
#    Then Search results for tea are shown

#  Scenario: User can search for a mug on Target
#    Given Open Target main page
#    When Search for mug
#    Then Search results for mug are shown

#  Scenario Outline: User can search for a product
#    Given Open Target main page
#    When Search for <product>
#    Then Search results for <product_result> are shown
#    Examples:
#    |product  |product_result |
#    |tea      |tea            |
#    |mug      |mug            |
#    |coffee   |coffee         |
##
#
#
#
#
#
#
#
# Feature: Target Cart Page
#   Enter feature description here
#
#  Scenario: User can see Empty Cart message
#    Given Open target main page
#    When Click on Cart Icon
#    Then Empty Cart message is shown
#
#
#  Scenario: Verify logged out user can navigate sign in
#    Given Open target main page
#    When Click sign In
#    Then From right side navigation menu, click Sign In
#    And Verify Sign In form opened

#Homework#4

#Feature: target circle page
#
#Scenario: User Open target circle page
#    Given Open target circle page
#    Then Verify two story cards under unlock added value
#
#Feature: add target product to cart
#
#  Scenario: User Open target circle page
#    Given Open target main page
#    When Search for product
#    Then add product to cart
#    Then view cart and checkout
#    Then Verify cart has individual item

#Homework #5

#Feature: Tests for product page
#
#    Scenario: Verify user can select color
#        Given Open target product A-84173947 page
##        When click on shirt color
#        Then Verify user can click through colors

#  Homework #6 #2

Feature: Tests for empty cart

    Scenario: Verify Your cart is empty message is shown for empty cart
      Given Open Target main page
      When Click on cart icon
      Then Verify your cart is empty message is shown


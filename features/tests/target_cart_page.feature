### Created by Mr. Blakes Kids at 1/12/2026
#Feature: Target Cart Page
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

Feature: target circle page

Scenario: User Open target circle page
    Given Open target circle page
    Then Verify two story cards under unlock added value

Feature: add target product to cart

  Scenario: User Open target circle page
    Given Open target main page
    When Search for product
    Then add product to cart
    Then view cart and checkout
    Then Verify cart has individual item

#Homework #5

#Feature: Tests for product page
#
#    Scenario: Verify user can select color
#        Given Open target product A-84173947 page
##        When click on shirt color
#        Then Verify user can click through colors


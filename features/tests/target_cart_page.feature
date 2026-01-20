## Created by Mr. Blakes Kids at 1/12/2026
Feature: Target Cart Page
   Enter feature description here

  Scenario: User can see Empty Cart message
    Given Open target main page
    When Click on Cart Icon
    Then Empty Cart message is shown


  Scenario: Verify logged out user can navigate sign in
    Given Open target main page
    When Click sign In
    Then From right side navigation menu, click Sign In
    And Verify Sign In form opened





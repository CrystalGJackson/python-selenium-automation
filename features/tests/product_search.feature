Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input tea into search field
    And Click on search icon
    Then Product results for tea are shown

Feature: Test Scenarios for Target functionality



@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

@then ('Empty cart message is shown')
   def verify_empty_cart_msg(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='emptyCartContainer']").text
    assert 'Your cart is empty' in actual_text, f"Expected 'Your cart is empty' text not in {actual_text}"
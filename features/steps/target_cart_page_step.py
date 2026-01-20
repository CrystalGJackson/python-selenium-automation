from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Homework 3 #1 Answer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



# Homework 3 #2 Answer

# @given('Open target main page')
# def open_main_page(context):
#     context.driver.get('https://www.target.com/')
#     sleep(5)
#
# @when('Click on Cart Icon')
# def click_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]').click()
#     sleep(5)
#
# @then('Empty Cart message is shown')
# def verify_empty_cart_message(context):
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
#     assert'your cart is empty' in actual_text.lower(), f"Expected 'your cart is empty'  text not in {actual_text}"
#     sleep(5)

# Homework 3 #3 Answer

@given('Open target main page')
def open_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when('Click sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='accountNav-signIn']").click()

@then('from right side navigation menu, click sign in')
def click_sign_in(context):
    context.driver.find_element(By.ID,"[a='account_sign_in']")
    assert'sign in form opened in actual_text,f"Expected sign in form opened" text not in {actual_text}'
    sleep(5)

@then('Verify sign in form opened')
def click_sign_in(context):
    context.driver.get('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_request_username&signin_amr=true')
    sleep(5)






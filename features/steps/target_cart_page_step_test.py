from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
#
#
#
# # Homework 3 #2 Answer
#
@given('Open target main page')
def open_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when('Click on Cart Icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]').click()
    sleep(5)

@then('Empty Cart message is shown')
def verify_empty_cart_message(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert 'your cart is empty' in actual_text.lower(), f"Expected 'your cart is empty'  text not in {actual_text}"
    sleep(5)

# Homework 3 #3 Answer

@when('Click sign In')
def click_sign_in(context):
    sleep(5)
    context.driver.find_element(By.ID, 'account-sign-in').click()
    sleep(5)
    #context.driver.find_element(By.ID, 'account-sign-in').click()

@then('From right side navigation menu, click Sign In')
def click_sign_in(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]').click()


@then('Verify Sign In form opened')
def click_sign_in(context):
    sleep(10)
    actual_text = context.driver.find_element(By.CSS_SELECTOR,'h1').text
    assert 'Sign in or create account' in actual_text,f'Expected "Sign in or create account" but got {actual_text}'








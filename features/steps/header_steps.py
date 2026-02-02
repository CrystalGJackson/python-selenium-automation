from time import sleep
from behave import when, then, given
import webdriver_manager.chrome
from selenium.webdriver.common.by import By


CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test='@web/GlobalHeader/UtilityHeader/']")





# @given('Open target main page')
# def open_main_page(context):
#     context.driver.get('https://www.target.com/')
#     sleep(5)

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(10)
#
# @when('Click on cart icon')
# def click_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, '[*data-test="@web/CartIcon"]').click()
#     sleep(10)

# @then('Verify your cart is empty message is shown')
# def verify_empty_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, '[*data-test="boxEmptyMsg"]').click()
#     sleep(10)
    # assert len(links) == verify_empty_cart, f'Expected {verify_empty_cart} header links, but found {len(links)}'



@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)

@then('Verify {expected_amount} top header links are shown')
def verify_top_links_shown(context, expected_amount):

    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)

    assert len(links) == expected_amount, f'Expected {expected_amount} header links, but found {len(links)}'

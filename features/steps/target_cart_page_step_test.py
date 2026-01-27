from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
# #
# #
# #
# # # Homework 3 #2 Answer
# #
@given('Open target main page')
def open_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(5)
# #
# @when('Click on Cart Icon')
# def click_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]').click()
#     sleep(5)
#
# @then('Empty Cart message is shown')
# def verify_empty_cart_message(context):
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
#     assert 'your cart is empty' in actual_text.lower(), f"Expected 'your cart is empty'  text not in {actual_text}"
#     sleep(5)
#
# # Homework 3 #3 Answer
#
# @when('Click sign In')
# def click_sign_in(context):
#     sleep(5)
#     context.driver.find_element(By.ID, 'account-sign-in').click()
#     sleep(5)
#     #context.driver.find_element(By.ID, 'account-sign-in').click()
#
# @then('From right side navigation menu, click Sign In')
# def click_sign_in(context):
#     sleep(5)
#     context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]').click()
#
#
# @then('Verify Sign In form opened')
# def click_sign_in(context):
#     sleep(10)
#     actual_text = context.driver.find_element(By.CSS_SELECTOR,'h1').text
#     assert 'Sign in or create account' in actual_text,f'Expected "Sign in or create account" but got {actual_text}'

# Homework 4 Answer #2

@given('Open target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')
    sleep(5)


@then('Verify two story cards under unlock added value')
def click_on_story_card(context):
    story_cards =  context.driver.find_elements(By.CSS_SELECTOR,'a [data-test="@web/SlingshotComponents/common/Storycard"]')
    assert 2 == len(story_cards),f"Expected 2 story cards but got {len(story_cards)}"
    sleep(5)

# Homework 4 Answer #3

@when('Search for product')
def search_for_product(context):
    sleep(10)
    context.driver.find_element(By.ID,'search').send_keys('rice')
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()

@then('add product to cart')
def add_product_to_cart(context):
    sleep(10)
    context.driver.find_element(By.CSS_SELECTOR, '[id*="addToCartButtonOrTextIdFor"]').click()
    sleep(15)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/AddToCart/Fulfillment/ShippingSection"] button[id*="addToCartButtonOrTextId"]').click()


@then('view cart and checkout')
def view_cart_and_checkout(context):
    sleep(10)
    context.driver.find_element(By.CSS_SELECTOR, '[href="/cart"]').click()

@then('Verify cart has individual item')
def verify_cart_has_individual_item(context):
    #item_in_cart = context.driver.find_element(By.CSS_SELECTOR, '[class="h-text-lg"]').click()
    sleep(10)
    item_in_cart = context.driver.find_element(By.CSS_SELECTOR, '[href="/icons/Cart.svg#Cart"]').text
    assert 'item in cart' in item_in_cart,f"Expected individual 'item in cart' not in {item_in_cart}"
    sleep(20)

# class="h-text-lg"
# '[aria-label = "Add to cart for 4Sisters Butter Belle Buttery White Rice Pouch"]').click()
# id="addToCartButtonOrTextIdFor91699335"
# data - test = "cartItem-image"]').click()
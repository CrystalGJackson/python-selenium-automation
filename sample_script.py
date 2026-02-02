from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
# driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
#
# driver.find_element(By.XPATH, '//a[@href="/ref=ap_frn_logo"]')
# driver.find_element(By.ID, 'ap_email_login')
# driver.find_element(By.XPATH, "//input[@class='a-button-input']")
# driver.find_element(By.XPATH,"//input[@class='a-spacing-top-medium a-size-small legal-text']")
# driver.find_element(By.XPATH, "//input[@class='a-spacing-top-medium a-size-small legal-text']")
# driver.find_element(By.XPATH, "//input[@href='/gp/help/customer/account-issues/ref=unified_claim_collection?ie=UTF8']")
# driver.find_element(By.ID, 'auth-fpp-link-bottom')
# driver.find_element(By.XPATH, "//input[@class='fs-match-card-title full']")
# driver.find_element(By.ID, 'createAccountSubmit')


# # open the url
# driver.get('https://www.target.com/')
# # expected = 'sign in or create account'
# # actual = driver.find_element (By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
#
#
# driver.find_element (By.XPATH, "//input[text(@class, 'styles_ndsHeading')= 'sign in or create account']")
# driver.find_element (By.ID, 'login')
#
#
#
#
#
# populate search field
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('Car')
#
# wait for 4 sec
# sleep(4)
#
# # click search button
# driver.find_element(By.NAME, 'btnK').click()
#
# # verify search results
# assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# print('Test Passed')
#
# driver.quit()
#
# driver.wait.until(
#      EC.element_to_be_clickable(search_btn),
#
#  ).click()
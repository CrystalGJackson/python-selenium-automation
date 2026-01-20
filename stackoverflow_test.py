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

# open the URL
driver.get('https://stackoverflow.com/users/signup/')
sleep(3)
# Get Stack overflow for teams:
driver.find_element(By.XPATH,'//a[@target="_blank"]')
# Create Your Account:
driver.find_element(By.XPATH,'//h1{@class="flex--item fs-headline1 fw-bold lh-xs mb8 ws-nowrap"}')
# By clicking sign up, you agree:
driver.find_element(By.XPATH, '//div[@class="flex--item js-terms fs-caption fc-black-400 ta-left"]')
# Email:
driver.find_element(By.ID, "email")
# Password:
driver.find_element(By.ID, "password")
# Hidden eye:
driver.find_element(By.XPATH, '//svg[@aria-hidden="true"]')
# Sign up:
driver.find_element(By.ID,"submit-button")
# Sign up with Google:
driver.find_element(By.XPATH,"//button[@data-provider='google']")
# Sign up with git hub:
driver.find_element(By.XPATH,"//button[@data-provider='github']")


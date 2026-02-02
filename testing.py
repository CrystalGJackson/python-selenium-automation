from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver_path = ChromeDriverManager().install()

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://google.com")

sleep(5)
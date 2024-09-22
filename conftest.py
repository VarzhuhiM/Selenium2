from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--window-size=1920x1980")
    #chrome_options.add_argument("--no-sanbox")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    driver.find_element(By.NAME, 'email').send_keys("varzhuhi@gmail.com")  # Use a valid email
    driver.find_element(By.NAME, 'password').send_keys("123456#")  # Use the corresponding password
    driver.find_element(By.XPATH, '//input[@value="Login"]').click()





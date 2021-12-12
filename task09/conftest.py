import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser_driver():
    browser_driver = webdriver.Chrome(ChromeDriverManager)
    yield browser_driver
    browser_driver.quit()

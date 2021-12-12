import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser_driver():
    driver = webdriver.Chrome(ChromeDriverManager)
    yield driver
    driver.quit()

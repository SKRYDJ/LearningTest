from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://esia-portal1.test.gosuslugi.ru/'

    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(ExpC.presence_of_element_located(locator),
                                                      message=f"{locator} locator element not found")

    def find_elements(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(ExpC.presence_of_all_elements_located(locator),
                                                      message=f"{locator} locator of elements not found")

    def go_to_url(self):
        return self.driver.get(self.base_url)

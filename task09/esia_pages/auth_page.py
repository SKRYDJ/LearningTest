from .base_page import BasePage
from .locators import Esia_locators


class Esia_login(BasePage):
    def enter_login(self, login):
        field_login = self.find_element(Esia_locators.LOCATOR_ESIA_LOGIN_FIELD)
        field_login.send_keys(login)

    def enter_password(self, password):
        field_password = self.find_element(Esia_locators.LOCATOR_ESIA_PASSWORD_FIELD)
        field_password.send_keys(password)

    def click_login_button(self):
        self.find_element(Esia_locators.LOCATOR_ESIA_LOGIN_BUTTON).click()


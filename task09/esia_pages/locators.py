from selenium.webdriver.common.by import By

class Esia_locators:
    LOCATOR_ESIA_LOGIN_FIELD = (By.XPATH, "//input[@name='login']")
    LOCATOR_ESIA_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_ESIA_CHECKBOX_REMEMBER = (By.XPATH, "//label[@for='ufoPC']")
    LOCATOR_ESIA_LOGIN_BUTTON = (By.CSS_SELECTOR, "button.ui-button ui-widget button-big")

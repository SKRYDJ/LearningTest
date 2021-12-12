from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager)

class
driver.find_elements(By.XPATH, '//input')
driver.find_elements_by_xpath("//input[@name='login']").send_keys('LOGIN')
driver.find_elements_by_xpath("//input[@name='password']").send_keys('PASSWORD')
from selenium.webdriver.common.by import By
from pages.test_data import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username_value, password_value):
        username = self.driver.find_element(By.ID, USERNAME_FIELD)
        username.send_keys(username_value)

        password = self.driver.find_element(By.ID, PASSWORD_FIELD)
        password.send_keys(password_value)

        login_button = self.driver.find_element(By.XPATH, LOGIN_BUTTON)
        login_button.click()

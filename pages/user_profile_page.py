from selenium.webdriver.common.by import By
from pages.test_data import *
from utilities.utils import Utils


class UserProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        ut = Utils(self.driver)
        ut.assert_url(USER_PROFILE_URL)
        logout_button = self.driver.find_element(By.XPATH, LOGOUT_BUTTON)
        logout_button.click()
        ut.assert_url(LOGIN_URL)

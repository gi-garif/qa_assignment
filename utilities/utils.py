import random
import string
from selenium.webdriver.common.by import By
from pages.test_data import FLASH_MESSAGE


class Utils:
    def __init__(self, driver):
        self.driver = driver

    def assert_url(self, url):
        assert self.driver.current_url == url

    def assert_flash_message(self, message):
        flash_message = self.driver.find_element(By.ID, FLASH_MESSAGE)
        assert message in flash_message.text

    def assert_element_is_present(self, element_id):
        element = self.driver.find_element(By.XPATH, element_id)
        assert element.is_displayed()

    def random_value(self, length):
        return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

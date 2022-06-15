import pytest
from pages.test_data import *
from pages.login_page import LoginPage
from pages.user_profile_page import UserProfilePage
from utilities.utils import Utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.up = UserProfilePage(self.driver)
        self.ut = Utils(self.driver)

    def test_successful_login(self):
        self.lp.login(USERNAME, PASSWORD)
        self.ut.assert_url(USER_PROFILE_URL)
        self.ut.assert_flash_message(SUCCESSFUL_LOGIN)
        self.up.logout()

    def test_wrong_username(self):
        self.lp.login(self.ut.random_value(10), PASSWORD)
        self.ut.assert_url(LOGIN_URL)
        self.ut.assert_flash_message(INCORRECT_USERNAME)

    def test_wrong_password(self):
        self.lp.login(USERNAME, self.ut.random_value(10))
        self.ut.assert_url(LOGIN_URL)
        self.ut.assert_flash_message(INCORRECT_PASSWORD)

    def test_wrong_username_and_wrong_password(self):
        self.lp.login(self.ut.random_value(10), self.ut.random_value(10))
        self.ut.assert_url(LOGIN_URL)
        self.ut.assert_flash_message(INCORRECT_USERNAME)

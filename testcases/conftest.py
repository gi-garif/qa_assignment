import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.test_data import LOGIN_URL


@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(LOGIN_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

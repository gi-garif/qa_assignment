# credentials for UI tests
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

# locators
USERNAME_FIELD = "username"
PASSWORD_FIELD = "password"
LOGIN_BUTTON = "//*[@id='login']/button"
LOGOUT_BUTTON = "//*[@id='content']/div/a"
FLASH_MESSAGE = "flash"

# URLs
LOGIN_URL = "http://the-internet.herokuapp.com/login"
USER_PROFILE_URL = "http://the-internet.herokuapp.com/secure"

SINGLE_USER_API = "https://reqres.in/api/users/2"
REGISTER_API = "https://reqres.in/api/register"
LOGIN_API = "https://reqres.in/api/login"

# flash messages
SUCCESSFUL_LOGIN = "You logged into a secure area!"
INCORRECT_USERNAME = "Your username is invalid!"
INCORRECT_PASSWORD = "Your password is invalid!"

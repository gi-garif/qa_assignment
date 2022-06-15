import requests
from assertpy.assertpy import assert_that

from pages.test_data import *


def test_get_user():
    response = requests.get(SINGLE_USER_API)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    response_text = response.json()
    user_email = response_text['data']['email']

    assert_that(user_email).is_not_empty()
    return user_email


def test_register_user():
    user_email = test_get_user()
    user_password = "12345678"
    creds = {'email': user_email, 'password': user_password}

    response = requests.post(REGISTER_API, data=creds)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    response_text = response.json()
    token = response_text['token']

    assert_that(token).is_not_empty()
    return token, user_email, user_password


def test_login():
    token, user_email, user_password = test_register_user()
    creds = {'email': user_email, 'password': user_password}

    response = requests.post(LOGIN_API, data=creds)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()['token']).is_equal_to(token)

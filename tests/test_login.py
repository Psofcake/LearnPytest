#tests/test_login.py

from pages.login import LoginPage
from selenium import webdriver
import pytest


def test_login_success(driver):
    page = LoginPage(driver, 10)
    page.open()
    page.login("tomsmith","SuperSecretPassword!")
    flash_msg = page.get_flash_message()

    print(flash_msg)
    assert "You logged into a secure area!" in flash_msg
    assert "/secure" in page.current_url()

def test_login_wrong_password(driver):
    page = LoginPage(driver,10)
    page.open()
    page.login("tomsmith","wrong!")
    flash_msg = page.get_flash_message()

    print(flash_msg)
    assert "Your password is invalid!" in flash_msg
    assert "/login" in page.current_url()

def test_logout(driver):
    page = LoginPage(driver, 10)
    page.open()
    page.login("tomsmith","SuperSecretPassword!")
    page.logout()

    flash_msg = page.get_flash_message()
    print(flash_msg)

    assert "You logged out of the secure area!" in flash_msg
    assert "/login" in page.current_url()

LOGIN_CASES = [
    ("tomsmith","SuperSecretPassword!","You logged into a secure area!","/secure"),
    ("tomsmith","wrongPW","Your password is invalid!","/login"),
    ("wrongID","SuperSecretPassword!","Your username is invalid!","/login")
]

@pytest.mark.parametrize("username,pw,expected_txt,expected_url",LOGIN_CASES)
def test_login(driver,username,pw,expected_txt,expected_url):
    page = LoginPage(driver, 10)
    page.open()
    page.login(username,pw)
    flash_msg = page.get_flash_message()

    print(flash_msg)
    assert expected_txt in flash_msg
    assert expected_url in page.current_url()


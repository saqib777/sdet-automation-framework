import pytest

pytestmark = pytest.mark.ui

from pages.login_page import LoginPage


def test_invalid_login_shows_error(driver):
    page = LoginPage(driver)

    page.open()
    page.login("wrong", "wrong")

    error = page.get_error_message()

    assert "Your username is invalid" in error

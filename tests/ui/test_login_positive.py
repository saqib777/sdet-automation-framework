import pytest

pytestmark = pytest.mark.ui
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()

    assert login_page.is_login_successful()

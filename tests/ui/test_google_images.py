import pytest

pytestmark = pytest.mark.ui

from pages.google_home_page import GoogleHomePage


@pytest.mark.skip(reason="Google UI is unstable – kept for learning")
def test_google_image_search(driver):
    google_page = GoogleHomePage(driver)

    google_page.open()
    google_page.go_to_images()
    google_page.search("Selenium WebDriver")
    google_page.click_first_image()

    assert google_page.is_image_preview_open()

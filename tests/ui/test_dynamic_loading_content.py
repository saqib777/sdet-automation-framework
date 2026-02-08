import pytest

pytestmark = pytest.mark.ui

from pages.dynamic_loading_page import DynamicLoadingPage


def test_dynamic_loading_text_is_not_empty(driver):
    page = DynamicLoadingPage(driver)

    page.open()
    page.click_start()

    text = page.get_finish_text()

    assert text.strip() != ""

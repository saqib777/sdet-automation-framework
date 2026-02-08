import pytest

pytestmark = pytest.mark.ui

from pages.dynamic_loading_page import DynamicLoadingPage

@pytest.mark.smoke
@pytest.mark.regression
def test_dynamic_loading_example(driver):
    page = DynamicLoadingPage(driver)

    page.open()
    page.click_start()

    result = page.get_finish_text()
    assert result == "Hello World!"

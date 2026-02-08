
import pytest

pytestmark = pytest.mark.ui

from pages.checkbox_page import CheckboxPage


def test_checkbox_can_be_selected(driver):
    page = CheckboxPage(driver)

    page.open()
    page.select_checkbox()

    assert page.is_checkbox_selected()

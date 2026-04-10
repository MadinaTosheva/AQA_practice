import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://demoqa.com"

DOUBLE_CLICK_BUTTON_loc = "#doubleClickBtn"
CLICK_ME_BUTTON_loc = "div.mt-4:nth-child(4) button"
DINAMIC_CLICK_loc = '#dynamicClickMessage'
FULL_NAME_INPUT_loc = "#userName"
EMAIL_INPUT_loc = '#userEmail'

SELECT_VALUE_TEXT = "Select Option"

@pytest.fixture
def launch_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        yield page

        browser.close()


def test_task_01(launch_browser):
    page = launch_browser

    page.goto(f"{BASE_URL}/buttons")
    double_click_button = page.locator(DOUBLE_CLICK_BUTTON_loc).inner_text()
    assert double_click_button == "Double Click Me"


def test_task_02(launch_browser):
    page = launch_browser

    page.goto(f"{BASE_URL}/buttons")
    page.locator(CLICK_ME_BUTTON_loc).click()
    expect(page.locator(DINAMIC_CLICK_loc)).to_have_text("You have done a dynamic click")
    dynamic_click_message = page.locator(DINAMIC_CLICK_loc).inner_text()
    # expect(dynamic_click_message).to_have_text("You have done a right click")

    assert dynamic_click_message == "You have done a dynamic click"


def test_task_03(launch_browser):
    page = launch_browser

    page.goto(f"{BASE_URL}/text-box")
    user_name_input = page.locator(FULL_NAME_INPUT_loc)
    user_name_input.fill("Madina")

    user_email_input = page.locator(EMAIL_INPUT_loc)
    user_email_input.fill("test@gmail.com")

    print(f"Имя: {user_name_input.input_value()},\n"
          f"Email: {user_email_input.input_value()}")


def test_task_04(launch_browser):
    page = launch_browser

    page.goto(f"{BASE_URL}/select-menu")
    select_value_dropdown = page.get_by_text(SELECT_VALUE_TEXT, exact=True).all_inner_texts()
    print(select_value_dropdown)

import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://demoqa.com"

DOUBLE_CLICK_BUTTON_LOC = "#doubleClickBtn"
CLICK_ME_BUTTON_LOC = "div.mt-4:nth-child(4) button"
DINAMIC_CLICK_LOC = '#dynamicClickMessage'
FULL_NAME_INPUT_LOC = "#userName"
EMAIL_INPUT_LOC = '#userEmail'
CURRENT_ADDRESS_LOC = "#currentAddress-label"

SELECT_VALUE_LOC = "#withOptGroup"

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
    double_click_button = page.locator(DOUBLE_CLICK_BUTTON_LOC).inner_text()
    assert double_click_button == "Double Click Me"


def test_task_02(launch_browser):
    page = launch_browser

    page.goto(f"{BASE_URL}/buttons")
    page.locator(CLICK_ME_BUTTON_LOC).click()
    expect(page.locator(DINAMIC_CLICK_LOC)).to_have_text("You have done a dynamic click")
    dynamic_click_message = page.locator(DINAMIC_CLICK_LOC).inner_text()
    # expect(dynamic_click_message).to_have_text("You have done a right click")

    assert dynamic_click_message == "You have done a dynamic click"


def test_task_03(launch_browser):
    page = launch_browser

    page.goto(f"{BASE_URL}/text-box")
    user_name_input = page.locator(FULL_NAME_INPUT_LOC)
    user_name_input.fill("Madina")

    user_email_input = page.locator(EMAIL_INPUT_LOC)
    user_email_input.fill("test@gmail.com")

    print(f"Имя: {user_name_input.input_value()},\n"
          f"Email: {user_email_input.input_value()}")


def test_task_04(launch_browser):
    page = launch_browser

    page.goto(f"{BASE_URL}/select-menu")
    select_value_dropdown = page.locator(SELECT_VALUE_LOC)
    select_value_dropdown_list = select_value_dropdown.get_by_role("option")
    assert select_value_dropdown_list.count() == 0
    select_value_dropdown.click()
    assert select_value_dropdown_list.count() == 6

    print(select_value_dropdown_list.count())
    print(select_value_dropdown_list.all_inner_texts())
    print(select_value_dropdown_list.all_text_contents())

    assert "Optimus Prime" in select_value_dropdown_list.all_inner_texts(), "В списке нету опции - Optimus Prime"


def test_task_05(launch_browser):
    page = launch_browser

    page.goto(f"{BASE_URL}/text-box")
    current_address_input = page.locator(CURRENT_ADDRESS_LOC)

    print(current_address_input.inner_text())
    print(current_address_input.text_content())
    assert current_address_input.inner_text() == current_address_input.text_content()

    print(repr(current_address_input.inner_text()))  ## 'Current Address'
import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://the-internet.herokuapp.com"

HEADER_TITLE_loc = "#content h2"
USERNAME_loc = "#username"
PASSWORD_loc = "#password"
LOGIN_loc = "[type='submit']"
VALIDATION_ERROR_loc = "#flash"


@pytest.fixture
def launch_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        yield page

        browser.close()


def test_task_06(launch_browser):
    page = launch_browser

    page.goto(BASE_URL)
    header_loc = page.locator(HEADER_TITLE_loc)
    header_text = header_loc.inner_text()
    assert "Available Examples" == header_text
    expect(header_loc).to_contain_text(header_text)


def test_task_07(launch_browser):
    page = launch_browser

    page.goto(f"{BASE_URL}/login")
    page.locator(USERNAME_loc).fill("tomsmith ")
    page.locator(PASSWORD_loc).fill("SuperSecretPassword!")
    page.locator(LOGIN_loc).click()

    validation_error = page.locator(VALIDATION_ERROR_loc)
    expect(validation_error).to_be_visible()

    error_text = validation_error.inner_text()
    assert "Your username is invalid!" in error_text
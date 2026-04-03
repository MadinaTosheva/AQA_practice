from playwright.sync_api import sync_playwright, expect

URL = "https://demoqa.com"

DOUBLE_CLICK_BUTTON = "#doubleClickBtn"
CLICK_ME_BUTTON = "div.mt-4:nth-child(4) button"
DINAMIC_CLICK = '#dynamicClickMessage'
FULL_NAME_INPUT = "#userName"
EMAIL_INPUT = '#userEmail'

def task_01():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=1000)
        page = browser.new_page()
        page.goto(f"{URL}/buttons")

        double_click_button = page.locator(DOUBLE_CLICK_BUTTON).inner_text()
        print(double_click_button)
        assert double_click_button == "Double Click Me"


def task_02():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(f"{URL}/buttons")

        page.locator(CLICK_ME_BUTTON).click()
        expect(page.locator(DINAMIC_CLICK)).to_have_text("You have done a dynamic click")
        dynamic_click_message = page.locator(DINAMIC_CLICK).inner_text()
        # expect(dynamic_click_message).to_have_text("You have done a right click")

        assert dynamic_click_message == "You have done a dynamic click"


def task_03():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(f"{URL}/text-box")

        user_name_input = page.locator(FULL_NAME_INPUT)
        user_name_input.fill("Madina")
        # user_name_input.inner_text()

        user_email_input = page.locator(EMAIL_INPUT)
        user_email_input.fill("test@gmail.com")

        print(f"Имя: {user_name_input.input_value()},\n"
              f"Email: {user_email_input.input_value()}")



if __name__ == "__main__":
    task_03()
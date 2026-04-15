from playwright.sync_api import expect

from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.example1 = page.get_by_role("link", name="Example 1")
        self.start = page.get_by_role("button", name="Start")
        self.text = page.locator("#finish>h4")

    def go_to_example1(self):
        self.example1.click()

    def click_on_start_button(self):
        self.start.click()

    def expect_text_to_be_visible(self):
        expect(self.text).to_be_visible()

    def get_element_text(self):
        return self.text.inner_text()
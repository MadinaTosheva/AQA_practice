from playwright.sync_api import expect

from pages.base_page import BasePage


class HoverPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.img = page.locator('(//div[@class="example"]/div/img)[1]')
        self.hidden_text = page.locator('(//div[@class="figcaption"]/h5)[1]')

    def hover_mouse_on_element(self):
        self.img.hover()

    def wait_element_to_be_visible(self):
        expect(self.hidden_text).to_be_visible()

    def get_element_text(self):
        return self.hidden_text.inner_text()
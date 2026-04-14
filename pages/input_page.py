from pages.base_page import BasePage


class InputPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.input = page.locator("[type='number']")

    def fill_input_with(self, value):
        self.input.fill(value)

    def get_input_value(self):
        return self.input.input_value()

    def clear_input(self):
        self.input.clear()

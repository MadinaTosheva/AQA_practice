from pages.base_page import BasePage


class DropdownPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.dropdown = page.locator('#dropdown')
        self.selected_value = self.page.locator("#dropdown option:checked")

    def select_option(self, value):
        self.dropdown.select_option(value)

    def get_selected_text(self):
        return self.selected_value.text_content()
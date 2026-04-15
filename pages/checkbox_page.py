from pages.base_page import BasePage


class CheckboxPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.checkbox1 = page.locator("(//form[@id = 'checkboxes']/input)[1]")
        self.checkbox2 = page.locator("(//form[@id = 'checkboxes']/input)[2]")

    def is_checked(self):
        return self.checkbox2.is_checked()

    def is_unchecked(self):
        return self.checkbox1.is_checked()

    def check_outbox(self):
        self.checkbox1.check()

    def uncheck_outbox(self):
        self.checkbox2.uncheck()

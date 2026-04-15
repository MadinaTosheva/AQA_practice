from pages.base_page import BasePage


class AlertsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.alert = page.locator('[onclick="jsAlert()"]')

    def go_to_jsAllert(self):
        self.alert.click()

    def accept_allert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username = self.page.locator("#username")
        self.password = self.page.locator("#password")
        self.login_btn = self.page.get_by_role("button", name="Login")

    def get_page_url(self):
        return self.page.url

    def login_as(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()
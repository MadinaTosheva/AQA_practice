from pages.base_page import BasePage


class LoginSuccessPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.logout = page.get_by_role("link", name="Logout")

    def get_page_url(self):
        return self.page.url

    def logout(self):
        self.logout().click()


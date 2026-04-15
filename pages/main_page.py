from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.URL = "https://the-internet.herokuapp.com/"
        self.login = self.page.get_by_role("link", name="Form Authentication")
        self.checkbox = self.page.get_by_role("link", name="Checkboxes")
        self.dropdown = self.page.get_by_role("link", name="Dropdown")
        self.inputs = self.page.get_by_role("link", name="Inputs")
        self.hovers = self.page.get_by_role("link", name="Hovers")
        self.alerts = self.page.get_by_role("link", name="JavaScript Alerts")
        self.file_upload = self.page.get_by_role("link", name="File Upload")
        self.dynamic_loading = self.page.get_by_role("link", name="Dynamic Loading")

    def open_main_page(self):
        self.open(self.URL)

    def get_page_title(self):
        return self.page.title()

    def go_to_login(self):
        self.login.click()

    def go_to_checkboxes(self):
        self.checkbox.click()

    def go_to_dropdown(self):
        self.dropdown.click()

    def go_to_inputs(self):
        self.inputs.click()

    def go_to_hovers(self):
        self.hovers.click()

    def go_to_alerts(self):
        self.alerts.click()

    def go_to_fileUpload(self):
        self.file_upload.click()

    def go_to_dynamicLoading(self):
        self.dynamic_loading.click()
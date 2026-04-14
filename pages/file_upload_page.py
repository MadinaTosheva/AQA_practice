from pathlib import Path
from playwright.sync_api import expect

from pages.base_page import BasePage


class UploadFilePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.new_file = None
        self.set_file = page.locator("#file-upload")
        self.submit_file = page.locator("#file-submit")
        self.uploaded_file = page.locator("#uploaded-files")


    def create_txt_file(self, file_name):
        self.new_file = Path(file_name)

    def write_text_into_file(self, text):
        self.new_file.write_text(text)

    def upload_file(self):
        self.set_file.set_input_files(self.new_file)
        self.submit_file.click()

    def wait_uploaded_file_to_be_visible(self):
        expect(self.uploaded_file).to_be_visible()

    def get_file_name(self):
        return self.new_file.name

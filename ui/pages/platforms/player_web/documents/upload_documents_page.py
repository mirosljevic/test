from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from ui.pages.components import Button, Input
from .components import UploadDialog
from .__selectors__ import UploadDocumentsSelectors as Selectors


class UploadDocumentsPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Upload Documents Page", **kwargs)

    @locate(Button, selector=Selectors.tab_button, component_name="Upload Document Tab")
    def tab(self) -> Button: pass

    @locate(Input, selector=Selectors.add_file_input, component_name="Add File Input")
    def add_file_input(self) -> Input: pass

    @locate(Button, selector=Selectors.continue_button, component_name="Continue Button")
    def continue_button(self) -> Button: pass

    @locate(UploadDialog)
    def upload_dialog(self) -> UploadDialog: pass

    def add_document(self, file_path):
        self.add_file_input.locator.set_input_files(file_path)
        self.continue_button.click()
        self.upload_dialog.upload_button.click()

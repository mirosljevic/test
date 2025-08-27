from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import UploadDialogSelectors as Selectors


class UploadDialog(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Upload Dialog", **kwargs)

    @locate(Button, selector=Selectors.upload_button, component_name="Upload Button")
    def upload_button(self) -> Button: pass

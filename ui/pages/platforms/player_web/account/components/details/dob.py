from datetime import datetime
from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text
from ui.pages.locator import locate
from .__selectors__ import DobSelectors as Selectors


class DobDetails(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Date of Birth Details", **kwargs)

    @locate(Text, selector=Selectors.dob_value, name="DOB Value")
    def dob_value(self) -> Text: pass

    def get_dob(self) -> datetime:
        dob_text = self.dob_value.get_text().replace(" ", "")
        return datetime.strptime(dob_text, "%m/%d/%Y")

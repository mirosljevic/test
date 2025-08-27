from playwright.sync_api import Page
from ui.pages.base import BasePage
from ui.pages.locator import locate
from .components.details import (NameDetails, EmailDetails, PasswordDetails, SsnDetails, MobileDetails,
                                 AddressDetails, DobDetails, NotificationDetails)


class MyDetailsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, page_name="My Details Page")

    @locate(NameDetails)
    def name_details(self) -> NameDetails: pass

    @locate(EmailDetails)
    def email_details(self) -> EmailDetails: pass

    @locate(PasswordDetails)
    def password_details(self) -> PasswordDetails: pass

    @locate(SsnDetails)
    def ssn_details(self) -> SsnDetails: pass

    @locate(MobileDetails)
    def mobile_details(self) -> MobileDetails: pass

    @locate(AddressDetails)
    def address_details(self) -> AddressDetails: pass

    @locate(DobDetails)
    def dob_details(self) -> DobDetails: pass

    @locate(NotificationDetails)
    def notification_details(self) -> NotificationDetails: pass

    def wait_for(self):
        self.name_details.wait_for()
        self.email_details.wait_for()
        self.password_details.wait_for()
        self.ssn_details.wait_for()
        self.mobile_details.wait_for()
        self.address_details.wait_for()
        self.dob_details.wait_for()
        self.notification_details.wait_for()
        return self

    def update_profile(self, current_password=None, new_password=None, mobile=None):
        if new_password:
            self.password_details.edit_password(current_password, new_password)
        if mobile:
            self.mobile_details.edit_mobile(mobile)
        return self

    def get_profile(self):
        return {
            "name": self.name_details.name_value.get_text(),
            "email": self.email_details.email_value.get_text(),
            "ssn": self.ssn_details.ssn_value.get_text(),
            "mobile": self.mobile_details.get_mobile(),
            "address": self.address_details.get_address(),
            "dob": self.dob_details.get_dob()
        }
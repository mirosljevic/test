from ui.pages.locator import Selectors


class NameSelectors:
    container = Selectors(data_test_id="pc-profile-name")
    name_value = Selectors(default=".pc-font-semibold")


class EmailSelectors:
    container = Selectors(data_test_id="pc-profile-email")
    email_value = Selectors(default=".pc-font-semibold")


class PasswordSelectors:
    container = Selectors(data_test_id="pc-player-profile-password")
    edit_button = Selectors(data_test_id="pc-edit-button")
    current_password_input = Selectors(data_test_id="pc-current-password-input")
    new_password_input = Selectors(data_test_id="pc-new-password-input")
    confirm_password_input = Selectors(data_test_id="pc-confirm-password-input")
    save_button = Selectors(data_test_id="pc-save-password-button")


class SsnSelectors:
    container = Selectors(data_test_id="pc-profile-ssn")
    ssn_value = Selectors(default=".pc-pl-1")


class MobileSelectors:
    container = Selectors(data_test_id="pc-profile-mobile")
    mobile_value = Selectors(default=".pc-font-semibold")
    edit_button = Selectors(data_test_id="pc-edit-button")
    mobile_input = Selectors(data_test_id="pc-mobile-phone-input")
    save_button = Selectors(data_test_id="pc-mobile-phone-save-button")


class AddressSelectors:
    container = Selectors(data_test_id="pc-profile-address")
    address_value = Selectors(default=".pc-font-semibold")


class DobSelectors:
    container = Selectors(data_test_id="pc-date-of-birth")
    dob_value = Selectors(default=".pc-font-semibold")


class NotificationSelectors:
    container = Selectors(data_test_id="pc-notifications")
    checkboxes = Selectors(data_test_id=".cc-checkbox")
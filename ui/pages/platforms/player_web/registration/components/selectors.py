from dataclasses import dataclass
from ui.pages.locator import Selectors


@dataclass
class RegistrationInitSelectors:
    container = Selectors(data_test_id="pc-verify-email-modal")
    email_field = Selectors(data_test_id="pc-verify-email-input")
    continue_button = Selectors(data_test_id="pc-verify-email-button")


@dataclass
class VerifyEmailSelectors:
    container = Selectors(data_test_id="pc-verify-email-modal")
    verify_email_text = Selectors(default="text=Please Verify Your Email")


@dataclass
class CreateAccountSelectors:
    container = Selectors(data_test_id="pc-registration-modal")
    get_started_button = Selectors(mobile="button:has-text('Get Started')")
    email_field = Selectors(data_test_id="pc-email-input")
    password_field = Selectors(data_test_id="pc-password-input")
    continue_button = Selectors(data_test_id="pc-continue-button")
    first_name_field = Selectors(data_test_id="pc-first-name-input")
    last_name_field = Selectors(data_test_id="pc-last-name-input")
    date_of_birth_field = Selectors(data_test_id="pc-date-of-birth-input")
    ssn_last_four_field = Selectors(data_test_id="pc-ssn-last-four-input")
    mobile_phone_field = Selectors(data_test_id="pc-mobile-phone-input")
    address_field = Selectors(data_test_id="pc-address1-input")
    city_field = Selectors(data_test_id="pc-city-input")
    state_select = Selectors(data_test_id="pc-state-select")
    zip_code_field = Selectors(data_test_id="pc-zip-input")
    gender_radio_button = Selectors(default="div[name='registerGender']")
    personalised_offers_checkbox = Selectors(data_test_id="pc-personalised-offers-checkbox")
    accept_terms_checkbox = Selectors(data_test_id="pc-accept-terms-checkbox")
    register_button = Selectors(data_test_id="pc-register-button")


@dataclass
class WelcomeDialogSelectors:
    container = Selectors(data_test_id="pc-registration-modal")
    welcome_text = Selectors(default="h2:has-text('Welcome')")
    sign_in_button = Selectors(default="text=Sign In")
    close_button = Selectors(default="[aria-label='Close registration form']")
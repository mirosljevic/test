from dataclasses import dataclass
from ui.pages.locator import Selectors


@dataclass
class MainMenuSelectors:
    container = Selectors(default=".MuiToolbar-regular > div")
    menu_item = Selectors(default="a.MuiButton-text")
    hamburger_button = Selectors(mobile="[aria-label='Open Menu']")
    mobile_menu_popper = Selectors(mobile="[role='menu']")
    mobile_menu_item = Selectors(mobile="button.MuiButton-text")
    register_button = Selectors(mobile="button:has(:text('Register'))")
    sign_in_button = Selectors(mobile="button:has(:text('Sign In'))")


@dataclass
class UserControlSelectors:
    container = Selectors(default="id=i-lottery-account-info")
    register_button = Selectors(data_test_id="pc-register-button")
    sign_in_button = Selectors(data_test_id="pc-login-button")
    balance_label = Selectors(default="(//span[text()='Balance']/following-sibling::span)[last()]")
    balance_label_mobile = Selectors(data_test_mobile_id="pc-balance-value")
    points_label = Selectors(default="//span[text()='Points']/following-sibling::span")
    points_label_mobile = Selectors(data_test_mobile_id="pc-balance-value")
    first_name_label = Selectors(default="span.pc-text-phoenix-blue-azzurre")
    user_menu_button = Selectors(data_test_id="pc-account-info-button",
                                 data_test_mobile_id="pc-account-info-mobile-button")
    user_menu_popper = Selectors(default=".popper", mobile=".pc-account-items-menu")
    user_menu_item = Selectors(default="button[data-test-id*='pc-account-info-item']",
                               mobile="button[data-test-id*='pc-account-info-mobile']")

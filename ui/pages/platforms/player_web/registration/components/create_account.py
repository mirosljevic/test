from playwright.sync_api import Page
from models import Player
from ui.pages.components import BaseComponent, Button, Input, DropDown, Radio, Checkbox
from ui.pages.locator import locate
from .selectors import CreateAccountSelectors as Selectors


class CreateAccount(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Create Account Modal", **kwargs)

    @locate(Button, selector=Selectors.get_started_button, component_name="Get Started Button")
    def get_started_button(self): pass

    @locate(Input, selector=Selectors.email_field, component_name="Email Field")
    def email_field(self): pass

    @locate(Input, selector=Selectors.password_field, component_name="Password Field")
    def password_field(self): pass

    @locate(Button, selector=Selectors.continue_button, component_name="Continue Button")
    def continue_button(self): pass

    @locate(Input, selector=Selectors.first_name_field, component_name="First Name Field")
    def first_name_field(self): pass

    @locate(Input, selector=Selectors.last_name_field, component_name="Last Name Field")
    def last_name_field(self): pass

    @locate(Input, selector=Selectors.date_of_birth_field, component_name="Date of Birth Field")
    def date_of_birth_field(self): pass

    @locate(Input, selector=Selectors.ssn_last_four_field, component_name="SSN Last Four Field")
    def ssn_last_four_field(self): pass

    @locate(Input, selector=Selectors.mobile_phone_field, component_name="Mobile Phone Field")
    def mobile_phone_field(self): pass

    @locate(Input, selector=Selectors.address_field, component_name="Address Field")
    def address_field(self): pass

    @locate(Input, selector=Selectors.city_field, component_name="City Field")
    def city_field(self): pass

    @locate(DropDown, selector=Selectors.state_select, component_name="State Select")
    def state_select(self): pass

    @locate(Input, selector=Selectors.zip_code_field, component_name="Zip Code Field")
    def zip_code_field(self): pass

    @locate(Radio, selector=Selectors.gender_radio_button, component_name="Gender Radio Button")
    def gender_radio_button(self): pass

    @locate(Checkbox, selector=Selectors.personalised_offers_checkbox, component_name="Personalised Offers Checkbox")
    def personalised_offers_checkbox(self): pass

    @locate(Checkbox, selector=Selectors.accept_terms_checkbox, component_name="Accept Terms Checkbox")
    def accept_terms_checkbox(self): pass

    @locate(Button, selector=Selectors.register_button, component_name="Register Button")
    def register_button(self): pass

    def wait_for(self):
        pass

    def submit_first_step(self, player: Player):
        if self.layout in ["mobile", "tablet"]:
            self.get_started_button.click()
        else:
            self.password_field.enter(player.password)
            self.continue_button.click()
        return self

    def submit_second_step(self, player: Player):
        if self.layout in ["mobile", "tablet"]:
            self.password_field.enter(player.password)
        self.first_name_field.enter(player.first_name)
        self.last_name_field.enter(player.last_name)
        self.date_of_birth_field.enter(player.date_of_birth.strftime('%m%d%Y'), typing=True)
        self.ssn_last_four_field.enter(player.ssn[-4:])
        self.mobile_phone_field(1).enter(player.phone)
        self.address_field.enter(player.address)
        self.city_field.enter(player.city)
        # self.state_select.enter(player.state)
        self.zip_code_field.enter(player.zip_code)
        self.gender_radio_button(player.gender.upper()).select()
        self.personalised_offers_checkbox.uncheck()
        self.accept_terms_checkbox.check()
        self.register_button.click()

    def submit_registration(self, player: Player):
        self.submit_first_step(player)
        self.submit_second_step(player)

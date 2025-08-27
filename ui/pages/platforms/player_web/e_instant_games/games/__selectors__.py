from ui.pages.locator import Selectors


class BaseGameSelectors:
    container = Selectors(default="body")
    labels = Selectors(default="#content > div > div:nth-of-type(2)")
    confirm_close_button = Selectors(default="text='Close Game'")
    bonus_play_button = Selectors(default="[aria-label=\"Let's Play\"]")
    bonus_close_button = Selectors(default="[aria-label='No, close game']")

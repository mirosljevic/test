from ui.pages.locator import Selectors


class MyAccountMenuSelectors:
    container = Selectors(default=".MuiPaper-elevation3 > ul[role='menu']", mobile="ul[role='list']")
    menu_item = Selectors(default=" li[role='menuitem']", mobile="li.MuiListItem-root")

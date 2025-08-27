from playwright.sync_api import Page, expect
from ui.pages.locator import Selectors
from environment import settings
from logger import log


class BaseComponent:
    def __init__(self,
                 page: Page,
                 selector: Selectors = None,
                 instance=None,
                 component_name: str = "Component",
                 layout=None,
                 tenant=None,
                 value=None,
                 index=None,
                 in_frame=False,
                 frame_locator=None,
                 **kwargs
                 ):
        self.page = page
        self.page_name = instance.page_name if instance else "Page"
        self.layout = layout if layout else instance.layout if instance else self._get_layout()
        self.tenant = tenant if tenant else instance.tenant if instance else settings.tenant.lower()
        self.parent_locator = instance.locator if instance else page
        self.instance = instance
        self.component_name = component_name
        self.selectors = selector
        self.index = index
        self.value = value
        self.exact_value = kwargs.get('exact_value', False)
        self.in_frame = in_frame or False
        self.frame_locator = frame_locator or (instance.frame_locator if instance else None) or "iframe"

    def __call__(self, *args):
        if args:
            if isinstance(args[0], int):
                self.index = args[0]
            elif isinstance(args[0], str):
                self.value = args[0]
            else:
                raise TypeError("Argument must be an int or str")
        return self

    def count(self):
        return self.locator.count()

    def is_unique(self):
        return self.count() == 1

    def exists(self, timeout=5_000):
        try:
            expect.set_options(timeout=timeout)
            expect(self.locator).to_have_count(1)
            log.debug(f"Component '{self.full_name_with_selector}' exists on the page.")
            return True
        except:
            log.warning(f"Component '{self.full_name_with_selector}' does not exist on the page.")
            return False

    @property
    def selector(self):
        if not self.selectors:
            if self.instance:
                return self.instance.selector
            else:
                raise ValueError("Selector must be provided or instance must be set")
        else:
            return self.selectors.get_selector(self.layout, self.tenant)

    @property
    def full_selector(self):
        if not self.selectors:
            return self.instance.full_selector
        else:
            return f"{self.instance.full_selector + ' > ' if self.instance and self.instance.full_selector else ''}{self.selector}"

    @property
    def full_name(self):
        return f"{self.instance.full_name if self.instance else self.page_name}.{self.component_name}"

    @property
    def full_name_with_selector(self):
        return f"{self.full_name} ({self.full_selector})"

    @property
    def locator(self):
        locator = self.parent_locator

        if self.in_frame:
            locator = locator.frame_locator(self.frame_locator)

        if self.selectors:
            locator = locator.locator(self.selector)

        if self.index is not None:
            locator = locator.nth(self.index)
        if self.value is not None:
            locator = locator.get_by_text(self.value, exact=self.exact_value)

        return locator

    def wait_for(self, timeout=5000):
        self.locator.wait_for(state='visible', timeout=timeout)

    def _get_layout(self):
        viewport = self.page.viewport_size
        if viewport:
            width = viewport.get('width', 0)
            if width <= 768:
                return "mobile"
            elif width <= 1024:
                return "tablet"
            else:
                return "desktop"


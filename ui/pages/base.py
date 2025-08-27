from playwright.sync_api import Page
from environment import settings


class BasePage:
    def __init__(self, page: Page, page_name: str = None, **kwargs):
        self.page = page
        self.page_name = page_name or "Page"
        self.layout = self._get_layout()
        self.tenant = settings.tenant.lower()
        self.frame_locator = None
        self.in_frame = False

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

    @property
    def locator(self):
        return self.page

    @property
    def full_name(self):
        return f"{self.page_name} ({self.layout})"

    @property
    def full_selector(self):
        return None

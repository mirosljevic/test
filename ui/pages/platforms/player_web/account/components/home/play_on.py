from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text
from ui.pages.locator import locate
from .__selectors__ import PlayOnSelectors as Selectors


class PlayOn(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Play On", **kwargs, index=1)

    @locate(Text, selector=Selectors.points, component_name="Points")
    def points(self) -> Text: pass

    @locate(Text, selector=Selectors.points_this_month, component_name="Points This Month", index=1)
    def points_this_month(self) -> Text: pass

    @locate(Text, selector=Selectors.draw_entries, component_name="Draw Entries", index=3)
    def draw_entries(self) -> Text: pass

    @locate(Text, selector=Selectors.second_chance, component_name="Second Chance", index=5)
    def second_chance(self) -> Text: pass

    def get_points(self) -> int:
        return int(self.points().get_text().replace("Pts", "").strip())

    def get_points_this_month(self) -> int:
        return int(self.points_this_month().get_text().replace("Pts", "").strip())

    def get_draw_entries(self) -> int:
        return int(self.draw_entries().get_text().replace("Entries", "").strip())

    def get_second_chance(self) -> int:
        return int(self.second_chance().get_text().replace("Entries", "").strip())

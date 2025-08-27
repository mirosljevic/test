from time import sleep
from logger import log
from .base import BaseComponent


class CanvasButton(BaseComponent):
    def __init__(self, page, component_name=None, game=None, instance=None, button=None, **kwargs):
        super().__init__(page=page, **kwargs)
        self.game = game
        self.button_name = button
        self.component_name = component_name
        self.percentages = instance.coordinates.get(button)
        self.frame_selector = instance.frame_locator or "iframe#ngl-rgs-game-container"
        self.canvas_selector = "canvas"

    @property
    def canvas(self):
        return self.page.frame_locator(self.frame_selector).locator(self.canvas_selector)

    @property
    def coordinates(self):
        x, y = self.get_coordinates()
        log.debug(f"Getting coordinates for {self.button_name}: x: {x}, y: {y}")
        return {"x": int(x), "y": int(y)}

    def _get_canvas_size(self):
        canvas_size = self.canvas.bounding_box()
        log.debug(f"Getting canvas size: {canvas_size}")
        return canvas_size

    def _get_cursor_style(self):
        cursor_style = self.canvas.evaluate("(e) => {return e.style.cursor }")
        log.debug(f"Getting cursor style: {cursor_style}")
        return cursor_style

    def get_coordinates(self):
        if not self.percentages:
            log.error(f"Coordinates for {self.component_name} button are not set.")
            raise ValueError

        canvas_size = self._get_canvas_size()
        x = canvas_size['width'] * (self.percentages[0] / 100)
        y = canvas_size['height'] * (self.percentages[1] / 100)
        log.debug(f"Calculated coordinates for {self.component_name}: x: {x}, y: {y}")
        return x, y

    def wait_for(self, retries=30):
        while retries > 0:
            try:
                self.canvas.hover(position=self.coordinates)
                cursor_style = self._get_cursor_style()
                if cursor_style == 'pointer':
                    log.debug(f"{self.component_name} is present at ({self.coordinates})")
                    return True
                else:
                    log.warning(
                        f"{self.component_name} is not clickable at ({self.coordinates}), cursor style: {cursor_style}")
            except Exception as e:
                log.error(f"Error while waiting for {self.component_name}: {e}")
            retries -= 1
            sleep(1)

    def is_displayed(self):
        displayed = self.wait_for()
        if displayed:
            log.debug(f"{self.component_name} is displayed at ({self.coordinates})")
        else:
            log.debug(f"{self.component_name} is not displayed at ({self.coordinates})")
        return displayed

    def click(self):
        log.debug(f"Clicking {self.component_name} at ({self.coordinates})")
        try:
            self.wait_for()
            self.canvas.click(position=self.coordinates)
            log.debug(f"{self.component_name} clicked at ({self.coordinates})")
        except Exception as e:
            log.error(f"Failed to click {self.component_name} at ({self.coordinates}): {e}")
            raise RuntimeError

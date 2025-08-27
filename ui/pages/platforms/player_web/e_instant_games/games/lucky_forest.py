from .base import BaseGame


class LuckyForest(BaseGame):
    def __init__(self, page, **kwargs):
        super().__init__(page, **kwargs)
        self.page_name = "Lucky Forest Game"
        self.coordinates = {
            'continue': (50, 74),
            'play': (70, 83),
            'cost_plus': (73, 72),
            'cost_minus': (63, 72),
            'reveal_all': (70, 83),
            'play_again': (70, 83),
            'close': (82, 8)
        }

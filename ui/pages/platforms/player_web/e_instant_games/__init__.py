from .instants import InstantsPage
from .games import BlackDiamondClub, LuckyForest, JungleCrossword
from .play_history import PlayHistoryPage


def Game(game, page):
    if game == "Lucky Forest":
        return LuckyForest(page)
    elif game == "Black Diamond Club":
        return BlackDiamondClub(page)
    elif game == "Jungle Crossword":
        return JungleCrossword(page)
    else:
        raise ValueError(f"Game '{game}' is not supported.")
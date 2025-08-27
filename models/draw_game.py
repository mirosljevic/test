from dataclasses import dataclass
from typing import Optional
from enum import Enum
from random import choice


@dataclass
class DrawGame:
    name: str
    game_id: str


class DrawGames:
    powerball = DrawGame("Powerball", "POWERBALL")
    mega_millions = DrawGame("Mega Millions", "MEGAMILLIONS")
    pick_3 = DrawGame("Pick 3", "PICK3")
    pick_4 = DrawGame("Pick 4", "PICK4")


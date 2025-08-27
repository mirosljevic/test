from dataclasses import dataclass
from typing import Optional, List
from enum import Enum
from random import choice


@dataclass
class InstantGame:
    name: str
    game_id: str
    demo_id: str


class InstantGames:
    primetime_payout = InstantGame("Primetime Payout", "PRIMETIME", "PRIMETIMEDEMO")
    tritons_treasures = InstantGame("Triton's Treasures", "TRITONSTREASURES", "TRITONSTREASURESDEMO")
    richcraft = InstantGame("Richcraft", "RICHCRAFT", "RICHCRAFTDEMO")
    cauldron_me_crazy = InstantGame("Cauldron Me Crazy", "CAULDRONMECRAZY", "CAULDRONMECRAZYDEMO")
    holiday_vip_riches = InstantGame("Holiday VIP Riches", "HOLIDAYVIPRICHES", "HOLIDAYVIPRICHESDEMO")
    hand_to_hand_tactics = InstantGame("Hand to Hand Tactics", "HANDTOHANDTACTICS", "HANDTOHANDTACTICSDEMO")
    black_diamond_club = InstantGame("Black Diamond Club", "BLACKDIAMONDCLUB", "BLACKDIAMONDCLUBDEMO")
    road_trip_riches = InstantGame("Road Trip Riches", "ROADTRIPRICHES", "ROADTRIPRICHESDEMO")
    inked_up = InstantGame("Inked Up", "INKEDUP", "INKEDUPDEMO")
    dragon_blast = InstantGame("Dragon Blast", "DRAGONBLAST", "DRAGONBLASTDEMO")
    diamond_flare = InstantGame("Diamond Flare", "DIAMONDFLARE", "DIAMONDFLAIREDEMO")
    mecha_bandit = InstantGame("Mecha Bandit", "MECHABANDIT", "MECHABANDITDEMO")
    corgi_cach_dash = InstantGame("Corgi Cach Dash", "CORGICACHDASH", "CORGICACHDASHDEMO")
    vip_reaches = InstantGame("VIP Reaches", "VIPREACHES", "VIPREACHESDEMO")
    crossbones_cash = InstantGame("Crossbones Cash", "CROSSBONESCASH", "CROSSBONESCASHDEMO")
    fruit_gone_bad = InstantGame("Fruit Gone Bad", "FRUITGONEBAD", "FRUITGONEBADDEMO")
    fast_track_cash = InstantGame("Fast Track Cash", "FASTTRACKCASH", "FASTTRACKCASHDEMO")
    prize_testing_game = InstantGame("Prize Testing Game", "TESTPRIZESHOT7S", "PRIZETESTINGGAMEDEMO")
    wildcat_riches = InstantGame("Wildcat Riches", "WILDCATRICHES", "WILDCATRICHESDEMO")
    jayhawk_riches = InstantGame("Jayhawk Riches", "JAYHAWKRICHES", "JAYHAWKRICHESDEMO")
    sizzling_hot_7s = InstantGame("Sizzling Hot 7s", "SIZZLINGHOT7S", "SIZZLINGHOT7SDEMO")
    lucky_forest = InstantGame("Lucky Forest", "LF", "LUCKYFORESTDEMO")
    jungle_crossword = InstantGame("Jungle Crossword", "JUNGLECROSSWORD", "JUNGLECROSSWORDDEMO")
    silver_fox_hunt = InstantGame("Silver Fox Hunt", "SILVERFOXHUNT", "SILVERFOXHUNTDEMO")
    teample_treasures = InstantGame("Teample Treasures", "TEAMPLTREASURES", "TEAMPLTREASURESDEMO")
    gold_rush = InstantGame("Gold Rush", "GOLDRUSH", "GOLDRUSHDEMO")
    bacon_me_crazy = InstantGame("Bacon Me Crazy", "BACONMECRAZY", "BACONMECRAZYDEMO")

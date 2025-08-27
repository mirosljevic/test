from requests import Session
from typing import Optional

from logger import log
from models import Player, InstantGame
from api.endpoints.igs_game.igs_game_web import game_step


class PlayerInstantsApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None):
        self.session = session
        self.player = player
        self.request_token = None
        self.session_id = None

    def init_game(self, game):
        response = game_step(session=self.session, game_id=game.game_id, method_name="startGameSession").json()
        self._update_session_and_token(response)
        return response

    def get_account_info(self, game: InstantGame) -> dict:
        response = game_step(
            session=self.session,
            game_id=game.game_id,
            method_name="getAccountInfo",
            request_token=self.request_token,
            session_id=self.session_id
        ).json()
        self._update_session_and_token(response)
        return response

    def start_play(self, game: InstantGame, cost, tickets, bonus=False, bonus_id=None) -> dict:
        response = game_step(
            session=self.session,
            game_id=game.game_id,
            method_name="bonusPlay" if bonus else "startPlay",
            request_token=self.request_token,
            session_id=self.session_id,
            method_parameters=[cost, tickets] if not bonus else [bonus_id, cost, tickets]
        ).json()
        self._update_session_and_token(response)
        return response

    def end_play(self, game: InstantGame) -> dict:
        response = game_step(
            session=self.session,
            game_id=game.game_id,
            method_name="endPlay",
            request_token=self.request_token,
            session_id=self.session_id
        ).json()
        self._update_session_and_token(response)
        return response

    def play_game(self, game: InstantGame, bonus=False, cost=None, tickets=None, highest_bet=False) -> dict:
        game_info = self.init_game(game)
        if not cost:
            if highest_bet:
                cost = game_info["result"]["betAmounts"][-1]
            else:
                cost = game_info["result"]["betAmounts"][0]
        tickets = tickets if tickets else game_info["result"]["playLevels"][0]

        account_info = self.get_account_info(game)
        bonus_id = account_info['result']['bonuses'][0]['id'] if bonus else None

        self.start_play(game, cost, tickets, bonus=bonus, bonus_id=bonus_id)
        self.end_play(game)
        return True

    def play_and_win(self, game, prize_amount=30, cost=None, tickets=None, highest_bet=False):
        game_info = self.init_game(game)
        if not cost:
            if highest_bet:
                cost = game_info["result"]["betAmounts"][-1]
            else:
                cost = game_info["result"]["betAmounts"][0]
        tickets = tickets if tickets else game_info["result"]["playLevels"][0]

        prize = 0
        while prize < prize_amount:
            self.start_play(game, cost, tickets)
            response = self.end_play(game)
            prize += response["result"]["totalPrizeAmount"]
            log.info(f"Won {prize} in {game.game_id} game")
        return True

    def play_demo(self, game: InstantGame, verify: bool = True) -> None:
        pass

    def get_play_sessions(self) -> None:
        pass



    def _update_session_and_token(self, response):
        self.request_token = response.get("clientRequestToken")
        self.session_id = response.get("clientSessionId")

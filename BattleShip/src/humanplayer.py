from . import player
from typing import List
from . import player,game_config


class HumanPlayer(player.Player):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"], type):
        super().__init__(player_num, config, other_players)
        self.init_name(player_num, other_players)
        self.place_ships()

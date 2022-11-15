from typing import List
import random
from . import aiplayer,game_config,move


class RandomAi(aiplayer.AIPlayer):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"], type):
        super().__init__(player_num, config, other_players, type)

    def get_move(self):
        coords=self.pick_coordinates()
        while True:
            try:
                firing_location = move.Move.from_str(self, coords)
            except ValueError as e:
                print(e)
                continue
            return firing_location

    def pick_coordinates(self):
        coord = random.choice(self.coordinates)
        row = str(coord[0])
        col = str(coord[1])
        self.coordinates.remove(coord)
        return(row + "," + col)
    
    

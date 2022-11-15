
from typing import List
from . import player, aiplayer, game_config,move

class CheatingAi(aiplayer.AIPlayer):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"], type):
        super().__init__(player_num, config, other_players,type)
        self.type=type

    def get_move(self):
        coords = self.pick_coordinates()
        while True:
            try:
                firing_location = move.Move.from_str(self, coords)
            except ValueError as e:
                print(e)
                continue
            return firing_location

    def pick_coordinates(self):
        self.enemy = self.opponents[0]
        coord=self.enemy.possible_hits[0]
        row = str(coord[0])
        col = str(coord[1])
        #row,col=coord.split(',')
        self.enemy.possible_hits.remove(coord)
        return (row + "," + col)



        
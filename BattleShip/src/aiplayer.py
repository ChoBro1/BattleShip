import random
from typing import List, Dict
from BattleShip.src import ship, orientation

from . import player, game_config, ship, ship_placement, move


class AIPlayer(player.Player):

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"], type):
        super().__init__(player_num, config, other_players)
        self.type = type
        # self.board_setup(player_num)

        # self.place_ship()

        self.name = None
        if self.type == "random":
            self.name = f"Random Ai {player_num}"
            self.place_ships()

        if self.type == "cheating":
            self.name = f"Cheating Ai {player_num}"
            self.place_ships()

        if self.type == "searchdestroy":
            self.name = (f"Search Destroy AI {player_num}")
            self.place_ships()

    def board_setup(self, player_num):
        if self.type == "random":
            self.name = f"Random Ai {player_num}"
            self.place_ships()
            return self.name

        if self.type == "cheating":
            self.name = f"Cheating AI {player_num}"
            self.place_ships()

        if self.type == "searchdestroy":
            self.name = (f"Search Destroy AI {player_num}")
            self.place_ships()

    # def get_coordinates(self):
    #     if self.type == "cheating":
    #         return self.get_moves(cheatingai.CheatingAI.pick_coordinates())
    #     if self.type == "searchdestroy":
    #         return SearchDestroyAI.pick_coordinates()

    def place_ship(self, ship_: ship.Ship) -> None:
        while True:
            placement = self.get_ship_placement(ship_)
            try:
                self.board.place_ship(placement)
            except ValueError as e:
                pass
            else:
                return


    def get_ship_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        return random.choice([orientation.Orientation.HORIZONTAL, orientation.Orientation.VERTICAL])

    def get_ship_start_coords(self, ship_: ship.Ship, orientation_: orientation.Orientation):

        if orientation_ == orientation.Orientation.HORIZONTAL:
            row = random.randint(0, self.board.num_rows - 1)
            col = random.randint(0, self.board.num_cols - ship_.length)
        else:
            row = random.randint(0, self.board.num_rows - ship_.length)
            col = random.randint(0, self.board.num_cols - 1)
        return row, col

    def place_ships(self) -> None:
        for ship_ in self.ships.values():
            self.display_placement_board()
            self.place_ship(ship_)
        self.display_placement_board()



    def get_ship_placement(self, ship_: ship.Ship):
        while True:
            try:
                orientation_ = self.get_ship_orientation(ship_)
                start_row, start_col = self.get_ship_start_coords(ship_, orientation_)
            except ValueError as e:
                print(e)
            else:
                return ship_placement.ShipPlacement(ship_, orientation_, start_row, start_col)

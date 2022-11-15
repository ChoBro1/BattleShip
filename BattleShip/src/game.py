import itertools,random
from . import game_config, player,humanplayer,randomai,cheatingai,searchdestroyai


class Game(object):

    def __init__(self, game_config_file: str,seed:int, num_players: int = 2,) -> None:
        super().__init__()
        random.seed(seed)
        self.game_config = game_config.GameConfig(game_config_file)
        self.players = []
        self.player_turn = 0
        self.setup_players(num_players)
        self.type=None


    def setup_players(self, num_players: int) -> None:
        for player_num in range(1, num_players + 1):
            while True:
                self.type = input(f"Enter one of ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi'] for Player {player_num}'s type: ")
                if self.type[0].lower() == "h":
                    if len(self.type)>7:
                        print(f'{self.type} does not represent any of the player types')
                        break
                    self.type = "human"
                    player=humanplayer.HumanPlayer(player_num, self.game_config, self.players,self.type)
                    self.players.append(player)
                    player.get_ship_coords()
                    #self.players.append(humanplayer.HumanPlayer(player_num, self.game_config, self.players,self.type))
                    break

                if self.type[0].lower() == "c":
                    if len(self.type)>10:
                        print(f'{self.type} does not represent any of the player types')
                        break
                    self.type = "cheating"
                    player = cheatingai.CheatingAi(player_num, self.game_config, self.players, self.type)
                    self.players.append(player)
                    player.get_ship_coords()
                    #self.players.append(aiplayer.AiPlayer(player_num, self.game_config, self.players,self.type))
                    break


                if self.type[0].lower() == "s":
                    if len(self.type)>15:
                        print(f'{self.type} does not represent any of the player types')
                        break

                    self.type = "searchdestroy"
                    player =searchdestroyai.SearchDestroyAi(player_num, self.game_config, self.players, self.type)
                    self.players.append(player)
                    player.get_ship_coords()
                    #self.players.append(aiplayer.AiPlayer(player_num, self.game_config, self.players, self.type))
                    break

                if self.type[0].lower() == "r":
                    if len(self.type)>8:
                        print(f'{self.type} does not represent any of the player types')
                        break

                    self.type = "random"
                    player=randomai.RandomAi(player_num, self.game_config, self.players, self.type)
                    
                    self.players.append(player)
                    player.get_ship_coords()
                    #self.players.append(randomai.RandomAi(player_num, self.game_config, self.players, self.type))
                    break

                else:
                    print(f'{self.type} does not represent any of the player types')








    def play(self) -> None:
        active_player = self.players[0]
        for active_player in itertools.cycle(self.players):
            self.do_current_players_turn(active_player) 
            if self.game_is_over():
                break
        print(f'{active_player} won the game!')

    def do_current_players_turn(self, cur_player: player.Player) -> None:
        self.display_gamestate(cur_player)
        while True:
                #print(cur_player.name)
                move = cur_player.get_move()
                #print(move)
                move.make()
                if move.ends_turn():
                    break

            #else:
             #   play=randomai.RandomAi
              #  move = play.move()
               # move.make()
                #if move.ends_turn():
                 #   break






    @property
    def num_players(self) -> int:
        return len(self.players)

    def get_active_player(self) -> player.Player:
        return self.players[self.player_turn]

    def game_is_over(self) -> bool:
        return any(player_.all_ships_sunk() for player_ in self.players)

    def display_gamestate(self, cur_player: player.Player) -> None:
        cur_player.display_scanning_boards()
        cur_player.display_firing_board()

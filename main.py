import sys
from BattleShip.src import game

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Not enough arguments given.')
    else:
        seed = int(sys.argv[2])
        #seed=2
        game_of_battle_ship = game.Game(sys.argv[1],seed)
        game_of_battle_ship.play()

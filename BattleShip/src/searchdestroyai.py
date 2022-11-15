from typing import List
import random
from . import aiplayer, game_config, move, randomai, ship, player


class SearchDestroyAi(aiplayer.AIPlayer):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"], type):
        super().__init__(player_num, config, other_players, type)
        self.list = []
        self.already_done = []
        self.mode= None

    def destroy_mode(self):
        self.mode="destroy"
        #print("desrtroy activated")
        #coords = self.pick_destroy()
        if len(self.list)==0:
            self.mode="search"
            return self.search_mode()

        coords = self.list[0]
        if coords in self.enemy.possible_hits:
            self.mode="destroy"
            self.add_coordinates(coords)

        row = str(coords[0])
        col = str(coords[1])
        new = (row + "," + col)
        self.list.remove(coords)
        #return new
        while True:
            try:
                firing_location = move.Move.from_str(self, new)
            except ValueError as e:
                print(e)
                continue
            return firing_location

    def search_mode(self):
        coord = random.choice(self.coordinates)
        if coord in self.enemy.possible_hits:
            self.mode = "destroy"
            self.add_coordinates(coord)
            return self.destroy_mode()
        else:
            row = str(coord[0])
            col = str(coord[1])
            self.coordinates.remove(coord)

            coords = (row + "," + col)

        while True:
            try:
                firing_location = move.Move.from_str(self, coords)
                #print(firing_location)
            except ValueError as e:
                print(e)
                continue
            return firing_location

    def add_coordinates(self,coords):
        x=coords[0]
        y=coords[1]
        ctr=(x,y)
        if ctr not in self.list:
            self.list.append(ctr)
            self.coordinates.remove(ctr)
        left=(x , y-1)
        if left in self.coordinates:
            self.coordinates.remove(left)
            if left not in self.list:
                    self.list.append(left)
        up = (x-1 , y)
        if up in self.coordinates:
            self.coordinates.remove(up)
            if up not in self.list:
                self.list.append(up)
        right = (x, y+1)
        if right in self.coordinates:
            self.coordinates.remove(right)
            if right not in self.list:
                self.list.append(right)
        down = (x+1 , y)
        if down in self.coordinates:
            self.coordinates.remove(down)
            if down not in self.list:
                self.list.append(down)

    def pick_destroy(self):
        if len(self.list)==0:
            self.mode="search"
            return self.search_mode()
        next_fire = self.list[0]
        if next_fire in self.enemy.possible_hits:
            self.mode="destroy"
            self.add_coordinates(next_fire)




        row = str(next_fire[0])
        col = str(next_fire[1])
        new = (row + "," + col)
        self.list.remove(next_fire)
        print (self.list)
        return new


    # def __init__(self,coordinates):
    #    self.coordinates= coordinates
    #   self.pick_coordinates()

    def pick_search(self):
        #coordinates = self.board.coordinate_list

        coord = random.choice(self.coordinates)
        if coord in self.enemy.possible_hits:
            self.mode="destroy"
            self.add_coordinates(coord)
            return self.destroy_mode()
        else:
            row = str(coord[0])
            col = str(coord[1])
            self.coordinates.remove(coord)

            #coords = (row + "," + col)

            return (row + "," + col)


    def get_move(self):

        self.enemy = self.opponents[0]
        if self.mode== None:
            self.mode="search"
        if self.mode == "search":
            return self.search_mode()
        if self.mode=="destroy":
            return self.destroy_mode()
       #     if self.scan():
        #        self.mode="destroy"
         #       return destroy_mode()

            #else:

             #   return self.search_mode()



    def scan(self):
        self.enemy=self.opponents[0]
        for x in self.enemy.possible_hits:
            row=x[0]
            col=x[1]
            if self.enemy.board.contents[row][col]=="X":
                mode="destroy"
                self.enemy.possible_hits.remove(x)
                self.add_coordinates(row,col)
                self.already_done.append((row,col))
                return True
            else:
                mode="search"
                return False

        #for x in range(len(self.enemy.board.contents)):
         #   for y in range(len(self.enemy.board.contents[0])):
          #      if str(self.enemy.board.contents[x][y]) == "X":
           #         mode = "destroy"
            #        if (x, y) not in self.already_done:
             #           self.already_done.append((x, y))
              #          self.add_coordinates((x, y))
             #   else:
              #      mode="search"
        #if mode=="destroy":
         #   return True















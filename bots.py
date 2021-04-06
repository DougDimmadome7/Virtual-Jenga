import copy
import random as r
 
class StatBot:
    """
    Meant mostly for testing and collecting interesting data on the game.
    """
    
    def is_valid(self, layer: int, index: int, tower) -> bool:
        """
        Given a piece to move on a certain tower, check if that piece results
        in the tower falling over.
        """
        tower = copy.deepcopy(tower)
        tower.move_piece(layer, index)
 
        if tower.will_fall():
            del tower
            return False
        else:
            del tower
            return True
 
    def all_valid(self, tower) -> int:
        """
        Returns the number of possible moves which don't cause collapse.
        """
        count = 0
        for layer in range(1, len(tower.tower)):
            for index in range(1, 4):
                if self.is_valid(layer, index, tower):
                    count += 1
 
        return count
 
class RandomBot:
    def __init__(self):
        self.stat_brain = StatBot()
 
    def __find_random_moves(self, tower) -> int:
        """
        Finds a random piece that exists, then returns it.
        """
        while True:
            height, index = r.randint(1, len(tower.tower)-1), r.randint(1,3)
            if tower.tower[height-1].blocks[index-1] == 1:
                return height, index
 
    def __find_all_moves(self, tower) -> list:
        """
        Returns a list of all valid pieces which won't cause the tower to 
        collapse.
        """
        choice = []
        for height in range(1,len(tower.tower)-2):
            for index in range(1,4):
                if self.stat_brain.is_valid(height, index, tower):
                    choice.append((height, index))
        
        r.shuffle(choice)
        return choice
 
 
    def make_move(self, tower):
        """
        Returns a random valid move.
        """
        height, index = self.__find_random_moves(tower)
 
        if self.stat_brain.all_valid(tower) == 0 or self.stat_brain.is_valid(height, index, tower):
            return height, index
        else:
            while not self.stat_brain.is_valid(height, index, tower):
                height, index = self.__find_random_moves(tower)
        
        return height, index
 
    def is_loose(self, layer, index) -> bool:
        y_n = input("Is piece {}, {} loose? ".format(layer, index))
        if y_n.lower() == "yes" or y_n.lower() == 'y':
            return True
        elif y_n.lower() == "no" or y_n.lower() == 'n':
            return False
 
    def turn(self, tower):
        choices = self.__find_all_moves(tower)
        valid_move = False
        print("Bot's turn")
 
        for choice in choices:
            picked = choice
            if self.is_loose(picked[0], picked[1]):
                valid_move = True
                break
 
        if valid_move:
            tower.move_piece(height, index)
            tower.display()
            return True
        else:
            return False
              
 

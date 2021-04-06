# WARNINGS: Make sure that the bot doesn't remove all blocks from a row.
import math
 
class Layer:
    def __init__(self, vertical = False, full = True):
        self.vertical = vertical
        self.blocks = [1, 1, 1] if full == True else [1, 0, 0]
    
    def get_mass(self) -> int:
        """ Returns the layer's mass"""
        return sum(self.blocks)
 
    def get_COM(self) -> tuple:
        """
        Finds the center of mass for the layer.
        """
        pos = 0
        for i in range(len(self.blocks)):
            if self.blocks[i] == 1:
                pos += i
        
        if self.vertical:
            return (pos/self.get_mass(), 1)
        else:
            return (1, pos/self.get_mass())
 
    def will_support(self, COM: list) -> bool:
        """
        Given the center of mass of some object resting on the layer, 
        this will determine whether or not it would fall off the layer.
        """
        if self.blocks == [1,0,1]:
            return True
 
        if self.vertical and self.blocks[round(COM[0])] == 0:
            return False
        elif not self.vertical and self.blocks[round(COM[1])] == 0:
            return False
        else:
            return True
            
    def add_block(self):
        for i in range(len(self.blocks)):
            if self.blocks[i] == 0:
                self.blocks[i] = 1
                break
        
    def display(self):
        if self.vertical:
            for i in range(len(self.blocks)):
                print("{} {} {}".format(self.blocks[0], self.blocks[1], self.blocks[2]))
        else:
            for i in range(len(self.blocks)):
                print("{} {} {}".format(self.blocks[2-i], self.blocks[2-i], self.blocks[2-i]))
 
class Tower:
    def __make_tower(self, height):
        """
        Creates the representation of the tower.
        """
        tower = []
        vertical = False
        for i in range(height):
            tower.append(Layer(vertical))
            vertical = True if vertical == False else False #flip the orientation
 
        return tower
 
    def __init__(self, height):
        self.height = height
        self.tower = self.__make_tower(self.height)
 
    def add_layer(self):
        self.tower.append(Layer(not self.tower[-1].vertical, False))
 
    def __weighted_average(self, tup1, tup2, m1, m2) -> tuple:
        """
        Given two tuples of COM and their respective masses, finds the 
        composite COM.
        """
        total_m = m1 + m2
        return (((m1/total_m)*tup1[0] + (m2/total_m)*tup2[0]), ((m1/total_m)*tup1[1] + (m2/total_m)*tup2[1]))
 
    def will_fall(self) -> bool:
        """
        Determines whether or not the tower, in its current configuration, will 
        collapse.
        """
        
        COM = (0,0)
        mass = 0
        top_t_bottom = self.tower.copy()
        top_t_bottom.reverse()
        for layer in top_t_bottom:
            if mass > 0 and not layer.will_support(COM):
                return True
 
            COM = self.__weighted_average(COM, layer.get_COM(), mass, layer.get_mass())
            mass += layer.get_mass()
        
        return False
 
    def move_piece(self, height, index):
        """
        Take a piece given and move it to the top.
        """
 
        assert height != len(self.tower)
        assert index < 4 and index > 0
 
        self.tower[height-1].blocks[index-1] = 0
 
        if self.tower[-1].get_mass() < 3:
            self.tower[-1].add_block()
        else:
            self.add_layer()
 
    def display(self):
        for i in range(1, len(self.tower)+1):
            self.tower[-i].display()
            print(" ")
 
 

import numpy as np
import random

class Land:

    def __init__(self, width, height, level):
        self.surface = np.zeros((width, height))
        self.set_fruit()
        self.set_obstacles()
        self.level = level

    def set_obstacles(self):

        for i in range(self.level):
        
        # depende del nivel, pero por ahora solo va a ser una cantidad fija
            x =random.randint(0, self.surface.shape[0])
            y=random.randbytes(0, self.surface.shape[1])

            self.surface[x,y] = 1








        

    def set_fruit(self):
        pass

    def set_snake(self):
        pass


    def update(self):
        pass

    

from game import Game
from land import Land
from snake import Snake

class Snake_Game(Game):
    
    def __init__(self, surface_width, surface_height):
        self.surface = Land(surface_width, surface_height, 0)
        self.snake = self.surface.set_snake()
   
    def run(self):
        pass


    def game_over(self):
        return self.snake.die

   
    def update(self):
        pass

    
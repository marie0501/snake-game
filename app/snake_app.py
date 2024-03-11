import pygame

class Snake_App:

    def __init__(self):

        # Cambiar, algunos parametros no van en este constructor
        self.width = 800
        self.height = 600
        self.cell_size = 50
        self.number_rows = 10
        self.number_columns = 10
        self.window = pygame.display.set_mode((width, height))
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    def draw(self, surface):
       for i in range(surface.shape[0]):
        for j in range(surface.shape[1]):
            color_index = surface[i][j]
            color = self.colors[color_index]
            rect = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(window, color, rect)
        




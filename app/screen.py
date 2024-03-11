import pygame

class Screen:
    def __init__(self, width, height, id):
        self.width = width
        self.height = height
        self.id = id

        # Define los colores que utilizarás
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.gray = (150, 150, 150)

    def draw(self, surface):
        surface.fill(self.white)
        text_surface = self.font.render('Segunda Pantalla', True, self.black)
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
        surface.blit(text_surface, text_rect)
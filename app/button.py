import pygame

class Button:

    def __init__(self, x, y, width, height, color, hover_color, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.hovered = False

        # Define los colores que utilizarás
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.gray = (150, 150, 150)

    def draw(self, surface):
        if self.hovered:
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        
        pygame.draw.rect(surface, self.gray, self.rect, 3)  # Borde

        if self.text != '':
            text_surface = self.font.render(self.text, True, self.black)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            self.hovered = True
        else:
            self.hovered = False
        return self.rect.collidepoint(pos)
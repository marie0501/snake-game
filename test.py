import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tamaño de la pantalla
WIDTH, HEIGHT = 800, 600

# Definir la clase Button
class Button:
    def __init__(self, x, y, width, height, color, text, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Función para la pantalla de inicio
def start_screen():
    screen.fill(WHITE)

    start_button = Button(300, 200, 200, 100, GREEN, "Start", BLACK)
    start_button.draw(screen)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(pygame.mouse.get_pos()):
                    return

# Función para la pantalla del juego
def game_screen():
    screen.fill(WHITE)

    # Simplemente dibujamos dos rectángulos para representar el score y la serpiente
    pygame.draw.rect(screen, BLACK, (50, 50, 200, 500))  # Columna del marcador
    pygame.draw.rect(screen, BLACK, (300, 50, 450, 500))  # Columna de la serpiente

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Configurar la pantalla principal
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Bucle principal
while True:
    start_screen()  # Mostrar pantalla de inicio
    game_screen()   # Mostrar pantalla del juego

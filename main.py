import pygame
import sys
from app.button import Button
from app.screen import Screen

if __name__=='__main__':
    pygame.init()

# define window size

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Botones con Pygame')
blocks = None


 # Define los colores que utilizarás
white = (255, 255, 255)
black = (0, 0, 0)
gray = (150, 150, 150)

button = Button(300, 200, 200, 100, white, gray, 'Start')
second_screen = Screen(width, height, 'second')
current_screen = 'main'

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            button.is_clicked(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Verifica si se hace clic con el botón izquierdo del mouse
                pos = pygame.mouse.get_pos()
                if button.is_clicked(pos):
                    current_screen = 'second'

    if current_screen == 'main':
        window.fill(white)
        button.draw(window)
    elif current_screen == 'second':
        window.fill(white)

        # Dibujar la palabra "Score" en la primera columna
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Score", True, black)
        text_rect = text_surface.get_rect()
        text_rect.centerx = 150
        text_rect.centery = 300
        window.blit(text_surface, text_rect)

        pygame.draw.rect(window, black, (300, 50, 450, 500), 3)  # Columna de la serpiente

        pygame.display.update()


    pygame.display.flip()


pygame.quit()
sys.exit()
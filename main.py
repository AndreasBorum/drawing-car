import pygame
import sys

from drawing_module import Drawing_surface
from car_module import Car_surface

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#----------------------------------------------

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse Coordinates Relative to Rectangle")


drawing_surface = Drawing_surface()
car_surface = Car_surface()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if drawing_surface.collide_rect .collidepoint(event.pos):
                drawing_surface.surface_clicked()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if drawing_surface.is_drawing:
                drawing_surface.surface_unclicked()
        

    # Clear the screen
    screen.fill(BLACK)


    drawing_surface.draw(screen)
    car_surface.draw(screen)



    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
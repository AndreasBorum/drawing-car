import pygame
import sys

from drawing_module import Drawing_surface
from car_surface import Car_surface
from explain_surface import Explain_surface
from button_module import Button

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 830
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#----------------------------------------------

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse Coordinates Relative to Rectangle")

start_drawing_btn = Button((80,40),(20,450))
next_point_btn = Button((80,40),(200,450))
drawing_surface = Drawing_surface()
# car_surface = Car_surface()
explain_surface=Explain_surface()

# def start_drawing():
    # car_surface.start_car(drawing_surface.dots)

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if drawing_surface.collide_rect.collidepoint(event.pos):
                drawing_surface.surface_clicked()
            # elif start_drawing_btn.collide_rect.collidepoint(event.pos):
                # start_drawing_btn.on_press(start_drawing)
            # elif next_point_btn.collide_rect.collidepoint(event.pos):
                # next_point_btn.on_press(car_surface.take_step)
            if explain_surface.collide_rect.collidepoint(event.pos):
                explain_surface.surface_clicked(event.pos)

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if drawing_surface.is_drawing:
                drawing_surface.surface_unclicked()
            if explain_surface.moving_car:
                explain_surface.moving_car=False
        if event.type == pygame.MOUSEWHEEL:
            if explain_surface.collide_rect.collidepoint(pygame.mouse.get_pos()):
                explain_surface.turn_car(event.y)
        

    # Clear the screen
    screen.fill(BLACK)


    drawing_surface.draw(screen)
    # car_surface.draw(screen, 0.1)
    explain_surface.draw(screen)
    start_drawing_btn.draw(screen)
    next_point_btn.draw(screen)

    clock.tick(60)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

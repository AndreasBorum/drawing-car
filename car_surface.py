import pygame

import colors
from car_calss import Car
from path_module import Path

SURFACE_SIZE = (400, 400)
SURFACE_POS = (420, 10)



class Car_surface():
    def __init__(self) -> None:
        self.surface = pygame.Surface(SURFACE_SIZE)
        self.rect = self.surface.get_rect()
        self.collide_rect = self.rect.move(SURFACE_POS)
        self.path_calculated = False 

        self.car = Car()
        self.animation_state = False
        self.animation_speed = 0.01



    def draw(self, parrent_surface):
        self.surface.fill(colors.light)

        if self.animation_state:
            self.animation_step()

        self.car.draw(self.surface)
        
        if self.path_calculated:
            self.path.draw(self.surface)

        parrent_surface.blit(self.surface, SURFACE_POS)

    def import_path_points(self, points):
        self.path = None
        self.path_points = points
        self.car.move_car(points[0], point='F')
        self.path = Path(points, self.car)
        self.path_calculated = True
        self.animation_pos =0
        self.animation_angle =0
        self.start_animation()

    def start_animation(self):
        if self.path_calculated:
            self.animation_state = True

    def stop_animation(self):
        self.animation_state = False

    def animation_step(self):
        self.animation_pos += self.animation_speed
        if self.animation_pos >= 1:
            self.animation_pos = 1
            self.stop_animation()

        pos, turn_angle = self.path.get_pos_on_path(self.animation_pos, self.animation_angle)

        self.car.move_car(pos,'F')
        self.car.turn_car(turn_angle, 'F')

        self.animation_angle += turn_angle
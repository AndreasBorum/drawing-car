import pygame

import math_module
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


    def draw(self, parrent_surface):
        #self.surface.fill('blue')

        #self.car.draw(self.surface)
        
        if self.path_calculated:
            self.path.draw(self.surface)

        parrent_surface.blit(self.surface, SURFACE_POS)

    def import_path_points(self, points):
        self.path = None
        self.path_points = points
        self.car.turn_car(5,'F',True)
        self.car.move_car(points[0], point='F')
        self.path = Path(points, self.car)
        print(self.path)
        self.path_calculated = False # turned off temp
        self.surface.fill('blue')
        self.car.draw(self.surface)
        self.path.draw(self.surface)

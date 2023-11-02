import pygame
import math
import numpy as np

from car_calss import Car
from helper import sub_tuple
from math_module import calculate_path


SURFACE_SIZE = (200, 400)
SURFACE_POS = (840, 10)


class Explain_surface():
    def __init__(self) -> None:
        self.surface = pygame.Surface(SURFACE_SIZE)
        self.rect = self.surface.get_rect()
        self.collide_rect = self.rect.move(SURFACE_POS)

        self.car = Car()
        self.car.pos = (100, 100)
        self.moving_car = False
        self.target_pos = (100, 200)

        self.update_path()


    def draw(self, parrent_surface):
        self.surface.fill('blue')

        # update car postion
        if self.moving_car:
            pos = pygame.mouse.get_pos()
            if self.collide_rect.collidepoint(pos):
                self.car.move_car(sub_tuple(pos, SURFACE_POS), 'center')
                self.update_path()

        # draw points
        pygame.draw.circle(self.surface, 'green', self.target_pos, 3)
        #pygame.draw.circle(self.surface, 'red', self.path['C'], 2)

        # draw circle path
        pygame.draw.circle(self.surface, (255, 0, 0, 0),
                           self.path['C'], self.path['radius'], 2)

        # draw intersection lines
        car_vectors = self.car.get_pos_vectors()
        pygame.draw.line(self.surface, 'white', self.path['C'], self.path['M'])
        pygame.draw.line(self.surface, 'white', self.path['C'],
                         car_vectors['centerW'])

        # draw angle lines
        pygame.draw.line(self.surface, 'yellow', self.path['C'], car_vectors['F'])
        pygame.draw.line(self.surface, 'yellow', self.path['C'], self.target_pos)

        self.car.draw(self.surface)

        # writes the angle as text on surface
        text1 = f"Angle: {round(self.path['angle_deg'],3)}"
        font = pygame.font.Font(None, 20)
        text_surface1 = font.render(text1, True, 'WHITE')
        self.surface.blit(text_surface1, (10, 10))

        text2 = f"Direction: {self.path['car_direction']}"
        text_surface2 = font.render(text2, True, 'WHITE')
        self.surface.blit(text_surface2, (10, 30))

        text3 = f"angle_direction: {self.path['angle_direction']}"
        text_surface3 = font.render(text3, True, 'WHITE')
        self.surface.blit(text_surface3, (10, 50))

        # draw to screen
        parrent_surface.blit(self.surface, SURFACE_POS)

    def surface_clicked(self, pos):

        if self.car.rect.move(SURFACE_POS).collidepoint(pos):
            self.moving_car = True

    def turn_car(self, direction):
        """turns car arund front point 5 degrees"""
        self.car.turn_car(direction*5, around='F', in_degrees=True)
        self.update_path()

    def update_path(self):
        """calculats the path"""
        car_vectors = self.car.get_pos_vectors()
        self.path= calculate_path(car_vectors, self.target_pos)

        # print(self.path['C'],M)
        self.wheel_line = self.make_line(car_vectors['LW'], car_vectors['RW'])
        # self.perpendicular_line =  self.make_line(self.path['C'], M)


    def make_line(self, piont1, point2):

        P1 = pygame.math.Vector2(piont1)
        P2 = pygame.math.Vector2(point2)

        M = (P1+P2)/2
        MP1 = P1-M
        MP2 = P2-M

        MP1.scale_to_length(SURFACE_SIZE[0]+SURFACE_SIZE[1])
        MP2.scale_to_length(SURFACE_SIZE[0]+SURFACE_SIZE[1])

        NP1 = M+MP1
        NP2 = M+MP2

        return (NP1, NP2)


import pygame

import math_module
from car_model import CAR_STRUCTUR_DICT, CAR_STRUCTUR_VECTORS_DICT

SURFACE_SIZE = (400, 400)
SURFACE_POS = (420, 10)


class Car_surface():
    def __init__(self) -> None:
        self.surface = pygame.Surface(SURFACE_SIZE)
        self.rect = self.surface.get_rect()
        self.collide_rect = self.rect.move(SURFACE_POS)

        self.points = []

        self.car_vectors = CAR_STRUCTUR_VECTORS_DICT

        self.surface.fill('blue')

    def draw(self, parrent_surface):

        for point in self.points:
            pygame.draw.circle(self.surface, 'white', point, 2)
        pygame.draw.polygon(self.surface, (0, 0, 0, 0), [value for value in self.car_vectors.values()], 3)

        parrent_surface.blit(self.surface, SURFACE_POS)

    def start_car(self, points):
        self.surface.fill('blue')
        self.points = points

        self.move_car(points[0], True)
        center, lenghts = math_module.find_intersect(
            points[0], points[1], *self.car_wheels())
        for lenght in lenghts:
            pygame.draw.circle(self.surface, (255, 0, 0, 0), center, lenght, 1)
        pygame.draw.circle(self.surface, 'red', center, 2)

    def move_car(self, pos, front=False):
        if front:
            self.car_vectors = {key: (coords+pos)-CAR_STRUCTUR_DICT['F'] for key, coords in CAR_STRUCTUR_VECTORS_DICT.items()}
        else:
            self.car_vectors = {key: coords+pos for key, coords in CAR_STRUCTUR_VECTORS_DICT.items()}

    def turn_car(self, angle):
        self.car_vectors = {key: vector.rotate(angle) for key, vector in self.car_vectors.items()}

    def car_wheels(self):
        R = tuple(map(lambda x, y: (x + y)/2,
                  self.car_vectors['I'], self.car_vectors['K']))
        L = tuple(map(lambda x, y: (x + y)/2,
                  self.car_vectors['A'], self.car_vectors['C']))
        return R, L

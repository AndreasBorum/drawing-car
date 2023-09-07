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
        self.at_point = 0

        self.car_vectors = CAR_STRUCTUR_VECTORS_DICT
        self.car_pos = (0,0)


    def draw(self, parrent_surface):
        self.surface.fill('blue')

        for point in self.points:
            pygame.draw.circle(self.surface, 'white', point, 2)
        pygame.draw.polygon(self.surface, (0, 0, 0, 0), [value for value in self.car_vectors.values()], 3)

        parrent_surface.blit(self.surface, SURFACE_POS)

    def start_car(self, points):
        self.surface.fill('blue')
        self.points = points

        self.move_car(points[0], True)
        center, lenghts, _ = math_module.find_intersect(
            points[0], points[1], *self.car_wheels())
        for lenght in lenghts:
            pygame.draw.circle(self.surface, (255, 0, 0, 0), center, lenght, 1)
        pygame.draw.circle(self.surface, 'red', center, 2)

    def path_to_next_point(self):
        center, lenghts, angle = math_module.find_intersect(self.points[self.at_point], self.points[self.at_point+1], *self.car_wheels())

    def move_car(self, pos, front=False):
        self.car_pos = pos
        if front:
            self.car_vectors = {key: (coords+pos)-CAR_STRUCTUR_DICT['F'] for key, coords in CAR_STRUCTUR_VECTORS_DICT.items()}
        else:
            self.car_vectors = {key: coords+pos for key, coords in CAR_STRUCTUR_VECTORS_DICT.items()}
        self.turn_car(1)


    def turn_car(self, angle):
        print('berfore turn: ', self.car_vectors)
        self.car_vectors = {key: vector.rotate_rad(angle)+self.car_pos for key, vector in CAR_STRUCTUR_VECTORS_DICT.items()}
        print('After turn: ', self.car_vectors)


    def car_wheels(self):
        R = tuple(map(lambda x, y: (x + y)/2,
                  self.car_vectors['I'], self.car_vectors['K']))
        L = tuple(map(lambda x, y: (x + y)/2,
                  self.car_vectors['A'], self.car_vectors['C']))
        return R, L



class car():
    def __init__(self):
        self.pos=(0,0)
        self.angle=0
        self.car_points_v = CAR_STRUCTUR_VECTORS_DICT


    def draw(self, surface):
        pygame.draw.polygon(surface, (0, 0, 0, 0), [value for value in self.car_points_v.values()], 2)

    def turn_car(self, turn_angle):
        self.car_points_v = {key: vector.rotate_rad(self.angle+turn_angle)+self.pos for key, vector in CAR_STRUCTUR_VECTORS_DICT.items()}

    def move_car(self, new_pos, front=False):
        self.pos = new_pos
        if front:
            self.car_points_v = {key: (coords+new_pos)-CAR_STRUCTUR_DICT['F'] for key, coords in CAR_STRUCTUR_VECTORS_DICT.items()}
        else:
            self.car_points_v = {key: coords+new_pos for key, coords in CAR_STRUCTUR_VECTORS_DICT.items()}
    
    def move_car_rel(self, pos_v, front=False):
        self.pos += pos_v
        if front:
            self.car_points_v = {key: (coords+pos_v)-CAR_STRUCTUR_DICT['F'] for key, coords in self.car_points_v.items()}
        else:
            self.car_points_v = {key: coords+pos_v for key, coords in self.car_points_v.items()}
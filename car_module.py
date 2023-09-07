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
        self.angle_between = 0
        self.angle_to_next = 0
        self.CL = None
        self.path_lines = []

        self.is_running = False
        self.car = Car()

        self.count = 0

    def draw(self, parrent_surface, speed):
        self.surface.fill('blue')

        for circle in self.path_lines:
            pygame.draw.circle(self.surface, (255, 0, 0, 0),
                               circle[0], circle[1], 1)

        if self.is_running:
            self.count += 1
            for point in self.points:
                pygame.draw.circle(self.surface, 'white', point, 2)
            if self.count < 20:
                self.take_step(speed)
            self.car.draw(self.surface)

        parrent_surface.blit(self.surface, SURFACE_POS)

    def take_step(self, speed):
        v, turn_angle, a = math_module.car_step(
            self.angle_between, self.path_lines[-1][1], self.angle_to_next, speed)
        if a == 0:
            print('at new point')
            self.at_point += 1
            self.path_to_next_point()
        else:
            self.angle_to_next = a
        self.car.move_car(self.CL.rotate_rad(self.angle_between-self.angle_to_next))
        #self.car.turn_car(turn_angle)

    def start_car(self, points):
        self.points = points

        self.car.move_car(points[0], True)
        self.path_to_next_point()

        self.is_running = True

    def path_to_next_point(self):
        if self.at_point == len(self.points):
            return
        else:
            center, lenghts, angle, _, self.CL  = math_module.find_intersect(
                self.points[self.at_point], self.points[self.at_point+1], *self.car.get_car_wheels())
            self.angle_between = angle
            self.angle_to_next = angle
            self.path_lines.append((center, lenghts[0], 0))


class Car():
    def __init__(self):
        self.pos = (0, 0)
        self.angle = 0
        self.car_points_v = CAR_STRUCTUR_VECTORS_DICT

    def draw(self, surface):
        pygame.draw.polygon(surface, (0, 0, 0, 0), [
                            value for value in self.car_points_v.values()], 2)

    def turn_car(self, turn_angle):
        self.angle += turn_angle
        print('car angle: ', self.angle)
        self.car_points_v = {key: vector.rotate_rad(
            -self.angle)+self.pos for key, vector in CAR_STRUCTUR_VECTORS_DICT.items()}

    def move_car(self, new_pos, front=False):
        self.pos = new_pos
        if front:
            self.car_points_v = {key: (
                coords+new_pos)-CAR_STRUCTUR_DICT['F'] for key, coords in CAR_STRUCTUR_VECTORS_DICT.items()}
        else:
            self.car_points_v = {key: coords+new_pos for key,
                                 coords in CAR_STRUCTUR_VECTORS_DICT.items()}

    def move_car_rel(self, pos_v, front=False):
        self.pos += pos_v
        if front:
            self.car_points_v = {key: (
                coords+pos_v)-CAR_STRUCTUR_DICT['F'] for key, coords in self.car_points_v.items()}
        else:
            self.car_points_v = {key: coords+pos_v for key,
                                 coords in self.car_points_v.items()}

    def get_car_wheels(self):
        R = tuple(map(lambda x, y: (x + y)/2,
                  self.car_points_v['I'], self.car_points_v['K']))
        L = tuple(map(lambda x, y: (x + y)/2,
                  self.car_points_v['A'], self.car_points_v['C']))
        return R, L

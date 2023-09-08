import pygame
from car_layout import CAR_STRUCTUR_DICT, CAR_STRUCTUR_VECTORS_DICT, L_V
import math

class Car():
    def __init__(self):
        self.pos = (0, 0)
        self.angle = 0
        self.car_points_v = CAR_STRUCTUR_VECTORS_DICT

    def draw(self, surface):
        pygame.draw.polygon(surface, (0, 0, 0, 0), [
                            value for value in self.car_points_v.values()], 2)

    def turn_car(self, turn_angle, in_degrees=False):
        
        self.angle += turn_angle if not in_degrees else math.radians(turn_angle)
        print('car angle: ', self.angle)
        self.car_points_v = {key: vector.rotate_rad(
            self.angle)+self.pos for key, vector in CAR_STRUCTUR_VECTORS_DICT.items()}

    def move_car(self, new_pos, front=False):
        print(f"car pos before: {self.car_points_v['A']}")
        if front:
            self.car_points_v = {key: (coords-self.pos+new_pos)-CAR_STRUCTUR_DICT['F'] for key, coords in self.car_points_v.items()}
        else:
            self.car_points_v = {key: coords-self.pos+new_pos for key,coords in self.car_points_v.items()}
        print(f"car pos after: {self.car_points_v['A']}")
        self.pos = self.car_points_v['A']

    def get_car_wheels(self):
        R = tuple(map(lambda x, y: (x + y)/2,
                  self.car_points_v['I'], self.car_points_v['K']))
        L = tuple(map(lambda x, y: (x + y)/2,
                  self.car_points_v['A'], self.car_points_v['C']))
        return R, L
    
    def set_car_wheels(self,R,L):
        old_R, old_L =[pygame.math.Vector2(whell) for whell in self.get_car_wheels()]
        angle=pygame.math.Vector2(old_L-old_R).angle_to(pygame.math.Vector2(L)-pygame.math.Vector2(R))
        self.turn_car(angle-180, True)
        self.move_car(R-L_V.rotate_rad(self.angle))


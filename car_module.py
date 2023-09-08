import pygame

import math_module
from car_model import CAR_STRUCTUR_DICT, CAR_STRUCTUR_VECTORS_DICT, L_V
import math

SURFACE_SIZE = (400, 400)
SURFACE_POS = (420, 10)



class Car_surface():
    def __init__(self) -> None:
        self.surface = pygame.Surface(SURFACE_SIZE)
        self.rect = self.surface.get_rect()
        self.collide_rect = self.rect.move(SURFACE_POS)

        
        self.center_points =[]
        self.points=[]
        self.is_drawing = False

        self.car = Car()

    def draw(self, parrent_surface, speed):
        self.surface.fill('blue')

        for point in self.points:
            pygame.draw.circle(self.surface, 'white', point, 2)
        
        if self.is_drawing:
            #self.take_step(speed)
            pygame.draw.polygon(self.surface, (0, 0, 0, 0), [value for value in self.car.car_points_v.values()], 3)

        for point in self.center_points:
            pygame.draw.circle(self.surface, 'red', point, 2)

        self.car.draw(self.surface)

        parrent_surface.blit(self.surface, SURFACE_POS)

    def take_step(self):
        speed=0.1

        old_L, old_R=self.car.get_car_wheels()

        R,L,self.current_angle= math_module.car_step(self.center_points[-1],old_R, old_L, self.angle_between_points,self.current_angle, speed)
        self.car.set_car_wheels(R,L)
        if self.current_angle==0:
            self.path_to_next_point()

    def start_car(self, points):
        self.points = points
        self.at_point=-1
        self.center_points =[]
        self.angle_between_points =0
        self.current_angle =0
        self.is_drawing = True
        
        self.car.car_points_v = CAR_STRUCTUR_VECTORS_DICT

        self.car.move_car(points[0],True)

        self.path_to_next_point()


    def path_to_next_point(self):
        self.at_point+=1
        center, self.angle_between_points= math_module.find_intersect(self.points[self.at_point], self.points[self.at_point+1], *self.car.get_car_wheels())
        self.center_points.append(center)

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


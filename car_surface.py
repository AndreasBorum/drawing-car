import pygame

import math_module
from car_calss import Car

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


    def draw(self, parrent_surface, speed):
        self.surface.fill('blue')

        for point in self.points:
            pygame.draw.circle(self.surface, 'white', point, 2)
        
        if self.is_drawing:
            #self.take_step(speed)
            self.car.draw(self.surface)

        for point, legnths in self.center_points:
            pygame.draw.circle(self.surface, 'red', point, 2)
            for radius in legnths:
                pygame.draw.circle(self.surface, (0,0,0,0), point, radius, 1)


        parrent_surface.blit(self.surface, SURFACE_POS)

    def take_step(self):
        speed=0.1

        old_L, old_R=self.car.get_car_wheels()
        R,L,self.current_angle= math_module.car_step(self.center_points[-1][0],old_R, old_L, self.angle_between_points,self.current_angle, speed)
        self.car.set_car_wheels(R,L)
        if self.current_angle==0:
            self.path_to_next_point()

    def start_car(self, points):
        self.car = Car()
        self.points = points
        self.at_point=-1
        self.center_points =[]
        self.angle_between_points =0
        self.current_angle =0
        self.is_drawing = True

        self.car.move_car(points[0],True)

        self.path_to_next_point()


    def path_to_next_point(self):
        self.at_point+=1
        if self.at_point < len(self.points)-1:
            center, self.angle_between_points, radius= math_module.find_intersect(self.points[self.at_point], self.points[self.at_point+1], *self.car.get_car_wheels())
            self.center_points = [(center,radius )]
        else:
            self.is_drawing = False
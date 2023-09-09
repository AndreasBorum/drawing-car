import pygame

import math_module
from car_calss import Car
from helper import sub_tuple

SURFACE_SIZE = (400, 400)
SURFACE_POS = (420, 10)



class Explain_surface():
    def __init__(self) -> None:
        self.surface = pygame.Surface(SURFACE_SIZE)
        self.rect = self.surface.get_rect()
        self.collide_rect = self.rect.move(SURFACE_POS)

        self.car = Car()
        self.car.pos=(100,100)
        self.moving_car=False

        self.target_pos = (200,200)
        self.wheel_line = ((0,0),(0,0))
        self.perpendicular_line =  ((0,0),(0,0))
        self.center = (0,0)
        self.cirkel_r = 0


    def draw(self, parrent_surface):
        self.surface.fill('blue')

        if self.moving_car:
            pos = pygame.mouse.get_pos()
            if self.collide_rect.collidepoint(pos):
                self.car.move_car(sub_tuple(pos, SURFACE_POS), 'center')
                self.update_path()

        pygame.draw.circle(self.surface,'green',self.target_pos,3)
        pygame.draw.circle(self.surface,'red',self.center,2)
        pygame.draw.circle(self.surface,(255,0,0,0),self.center,self.cirkel_r,2)

        self.car.draw(self.surface)
        

        # for point, legnths in self.center_points:
        #     pygame.draw.circle(self.surface, 'red', point, 2)
        #     for radius in legnths:
        #         pygame.draw.circle(self.surface, (0,0,0,0), point, radius, 1)


        parrent_surface.blit(self.surface, SURFACE_POS)

    def take_step(self):
        speed=0.1

        old_L, old_R=self.car.get_car_wheels()
        R,L,self.current_angle= math_module.car_step(self.center_points[-1][0],old_R, old_L, self.angle_between_points,self.current_angle, speed)

        center, self.angle_between_points, radius= math_module.find_intersect(self.points[self.at_point], self.points[self.at_point+1], *self.car.get_car_wheels())


    def surface_clicked(self, pos):
        print(self.car.rect.move(SURFACE_POS))
        if self.car.rect.move(SURFACE_POS).collidepoint(pos):
            self.moving_car = True
        
    
    def turn_car(self, direction):
        #print(f"tuning car: {direction}")
        self.car.turn_car(direction*5,around='F',in_degrees=True)
        self.update_path()

    def update_path(self):
        car_vectors = self.car.get_pos_vectors()
        self.center, _, self.cirkel_r= math_module.find_intersect(car_vectors['F'],self.target_pos,car_vectors['LW'],car_vectors['RW'])


            
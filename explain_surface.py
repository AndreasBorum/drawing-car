import pygame

import math_module
from car_calss import Car
from helper import sub_tuple
import math

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

        self.update_path()

        # self.wheel_line = ((0,0),(0,0))
        # self.perpendicular_line =  ((0,0),(0,0))
        # self.center = (0,0)
        # self.cirkel_r = 0
        # self.angle = 0


    def draw(self, parrent_surface):
        self.surface.fill('blue')

        #update car postion
        if self.moving_car:
            pos = pygame.mouse.get_pos()
            if self.collide_rect.collidepoint(pos):
                self.car.move_car(sub_tuple(pos, SURFACE_POS), 'center')
                self.update_path()

        #draw points
        pygame.draw.circle(self.surface,'green',self.target_pos,3)
        pygame.draw.circle(self.surface,'red',self.center,2)

        #draw circle path
        pygame.draw.circle(self.surface,(255,0,0,0),self.center,self.visuals['radius'],2)

        # draw intersection lines
        car_vectors = self.car.get_pos_vectors()
        pygame.draw.line(self.surface,'white',self.center,self.visuals['M'])
        pygame.draw.line(self.surface,'white',self.center,car_vectors['centerW'])

        #draw angle lines
        pygame.draw.line(self.surface,'yellow',self.center,car_vectors['F'])
        pygame.draw.line(self.surface,'yellow',self.center,self.target_pos)

        self.car.draw(self.surface)

        # writes the angle as text on surface
        text = f"Angle: {math.degrees(round(self.angle,3))}"
        font = pygame.font.Font(None, 20)
        text_surface = font.render(text, True, 'WHITE')
        self.surface.blit(text_surface, (10, 10))

        #draw to screen
        parrent_surface.blit(self.surface, SURFACE_POS)


    def surface_clicked(self, pos):

        if self.car.rect.move(SURFACE_POS).collidepoint(pos):
            self.moving_car = True
        
    
    def turn_car(self, direction):
        """turns car arund front point 5 degrees"""
        self.car.turn_car(direction*5,around='F',in_degrees=True)
        self.update_path()

    def update_path(self):
        """calculats the path"""
        car_vectors = self.car.get_pos_vectors()
        self.center , self.angle, self.visuals= math_module.find_intersect(car_vectors,self.target_pos)
        
        #print(self.center,M)
        self.wheel_line = self.make_line(car_vectors['LW'], car_vectors['RW'])
        #self.perpendicular_line =  self.make_line(self.center, M)

    def print_angle(self):
        """prints angle between front and target"""
        print(math.degrees(self.angle),' |--| ', self.angle)
    

    def make_line(self, piont1, point2):

        P1 = pygame.math.Vector2(piont1)
        P2 = pygame.math.Vector2(point2)

        M = (P1+P2)/2
        MP1= P1-M
        MP2= P2-M

        MP1.scale_to_length(SURFACE_SIZE[0]+SURFACE_SIZE[1])
        MP2.scale_to_length(SURFACE_SIZE[0]+SURFACE_SIZE[1])

        NP1= M+MP1
        NP2= M+MP2

        return (NP1, NP2)
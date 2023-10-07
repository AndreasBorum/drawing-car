import pygame
import math
import numpy as np

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
        self.car.pos = (100, 100)
        self.moving_car = False
        self.target_pos = (200, 200)

        self.update_path()

        # self.wheel_line = ((0,0),(0,0))
        # self.perpendicular_line =  ((0,0),(0,0))
        # self.center = (0,0)
        # self.cirkel_r = 0
        # self.angle = 0

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
        pygame.draw.circle(self.surface, 'red', self.center, 2)

        # draw circle path
        pygame.draw.circle(self.surface, (255, 0, 0, 0),
                           self.center, self.visuals['radius'], 2)

        # draw intersection lines
        car_vectors = self.car.get_pos_vectors()
        pygame.draw.line(self.surface, 'white', self.center, self.visuals['M'])
        pygame.draw.line(self.surface, 'white', self.center,
                         car_vectors['centerW'])

        # draw angle lines
        pygame.draw.line(self.surface, 'yellow', self.center, car_vectors['F'])
        pygame.draw.line(self.surface, 'yellow', self.center, self.target_pos)

        self.car.draw(self.surface)

        # writes the angle as text on surface
        text1 = f"Angle: {math.degrees(round(self.angle,3))}"
        font = pygame.font.Font(None, 20)
        text_surface1 = font.render(text1, True, 'WHITE')
        self.surface.blit(text_surface1, (10, 10))

        text2 = f"Direction: {self.direction}"
        text_surface2 = font.render(text2, True, 'WHITE')
        self.surface.blit(text_surface2, (10, 30))

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
        self.center, self.angle, self.visuals, self.direction = find_intersect(
            car_vectors, self.target_pos)

        # print(self.center,M)
        self.wheel_line = self.make_line(car_vectors['LW'], car_vectors['RW'])
        # self.perpendicular_line =  self.make_line(self.center, M)


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



def find_intersect(car_vectors, target):
    A = np.array(car_vectors['F'])
    B = np.array(target)
    R = np.array(car_vectors['RW'])
    L = np.array(car_vectors['LW'])

    AB = B-A
    M = (AB)/2+A
    v = np.array((-AB[1], AB[0]))
    LR= R-L


    # checks if the lines af parallel 
    if np.linalg.det([LR, v]) == 0:
        visuals ={'M':tuple(M), 'radius':0}
        return M, 0, visuals, 0

    # finder skæringspunktet
    s = np.cross(LR,(R-M))/np.cross(LR,v)
    t = np.cross(v,(M-np.array(car_vectors['centerW'])))/np.cross(v,LR)

    new_v = v*s
    C=new_v+M

    CA = A-C
    CB = B-C
    angle = np.arccos(CA.dot(CB)/(np.linalg.norm(CA)*np.linalg.norm(CB)))
    direction = 1 if np.sign(s)!=np.sign(t) else -1

    visuals ={'M':tuple(M), 'radius':np.linalg.norm(C-A)}

    return tuple(C), angle, visuals, direction
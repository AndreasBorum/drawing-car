import pygame

import math_module

SURFACE_SIZE = (400,400)
SURFACE_POS = (420,10)

car_structur_dict = {
    'A': (0, 0),
    'B': (0, 3),
    'C': (1, 3),
    'D': (1, 2),
    'E': (2, 3),
    'F': (3, 6),
    'G': (4, 3),
    'H': (5, 2),
    'I': (5, 3),
    'J': (6, 3),
    'K': (6, 0),
    'L': (5, 0),
    'M': (5, 1),
    'N': (1, 1),
    'O': (1, 0)
    }
car_structur_dict = {key: tuple(10 * value for value in coords) for key, coords in car_structur_dict.items()}

class Car_surface():
    def __init__(self) -> None:
        self.surface = pygame.Surface(SURFACE_SIZE)
        self.rect = self.surface.get_rect()
        self.collide_rect=self.rect.move(SURFACE_POS)

        self.points=[]

        self.car_structur_vectors =[]
        for point in car_structur_dict.values():
            self.car_structur_vectors.append(pygame.math.Vector2(point))
        self.car_vectors = self.car_structur_vectors
        

        self.surface.fill('blue')
    def draw(self, parrent_surface):

        for point in self.points:
            pygame.draw.circle(self.surface,'white',point,2)
        pygame.draw.polygon(self.surface,(0,0,0,0), self.car_vectors, 3)

        parrent_surface.blit(self.surface,SURFACE_POS)

    def start_car(self, points):
        self.surface.fill('blue')
        self.points=points

        self.move_car(points[0], True)
        center,lenghts=math_module.find_intersect(points[0],points[1], *self.car_wheels())
        for lenght in lenghts:
            pygame.draw.circle(self.surface,(255,0,0,0),center,lenght,1)
        pygame.draw.circle(self.surface,'red',center,2)

    def move_car(self,pos, front=False):
        if front:
            self.car_vectors = [point+pos-car_structur_dict['F'] for point in self.car_structur_vectors ]
        else:
            self.car_vectors = [point+pos for point in self.car_structur_vectors ]
    

    def turn_car(self, angle):
        self.car_vectors = [vector.rotate(angle) for vector in self.car_vectors]

    def car_wheels(self):
        R= tuple(map(lambda x, y: (x + y)/2, self.car_vectors[8], self.car_vectors[10]))
        L= tuple(map(lambda x, y: (x + y)/2, self.car_vectors[0], self.car_vectors[2]))
        return R, L


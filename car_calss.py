import pygame
import math
import numpy as np

from car_layout import CAR_STRUCTURE_VECTORS_DICT, SPECIAL_POINTS


class Car():
    def __init__(self):
        self.pos = (0, 0)
        self.angle = 0

        self.structure_vectors = CAR_STRUCTURE_VECTORS_DICT

    def draw(self, surface):
        """Draws the car on the surface"""
        self.rect = pygame.draw.polygon(surface, (0, 0, 0), [
                                        value for key, value in self.get_pos_vectors().items() if key not in SPECIAL_POINTS], 2)
        pygame.draw.circle(surface, 'white', self.pos, 2)

    def turn_car(self, turn_angle_, around, in_degrees=False):
        """turns the car arund a car scruture point"""

        # converts to radians
        if not in_degrees:
            turn_angle = turn_angle_
        else:
            turn_angle = math.radians(turn_angle_)

        # rotate the car
        from_other_point = {key: (vector-self.structure_vectors[around]).rotate_rad(
            turn_angle) for key, vector in self.structure_vectors.items()}
        self.structure_vectors = {
            key: vector+self.structure_vectors[around] for key, vector in from_other_point.items()}

        # update car posistion
        self.pos += self.structure_vectors['A']
        self.structure_vectors = {
            key: vector-self.structure_vectors['A'] for key, vector in self.structure_vectors.items()}

    def turn_car_outside_point(self, turn_angle_, around, in_degrees=False):
        """turns the car arund a point"""

        # converts to radians
        if not in_degrees:
            turn_angle = turn_angle_
        else:
            turn_angle = math.radians(turn_angle_)

        around_v = pygame.Vector2(around)

        # move car
        from_other_point = (self.pos-around_v).rotate_rad(turn_angle)
        self.pos = from_other_point+around_v

        # rotate car
        self.turn_car(turn_angle_, 'A', in_degrees)

    def move_car(self, new_pos, point='A'):
        """moves car, by moving a car point to new posistion"""
        self.pos = new_pos-self.structure_vectors[point]

    def get_pos_vectors(self):
        """returns vectors for car points relativ to surface"""
        return {key: coords + self.pos for key, coords in self.structure_vectors.items()}

    def move_turn_car(self, new_pos, direction_vector, angle_direction):  # arbejd her!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """moves the cars front point to new_pos, and aligns the car parralel to direction_vector"""
        


        angle = math.radians(pygame.Vector2(direction_vector).as_polar()[1])
        if angle_direction < 0:
            angle += math.radians(180)
        print(pygame.Vector2((1,0)).as_polar(),pygame.Vector2((0,1)).as_polar(),pygame.Vector2((1,1)).as_polar())

        
        
        

        # rotate the car
        from_other_point = {key: (vector-self.structure_vectors['F']).rotate_rad(
            angle) for key, vector in CAR_STRUCTURE_VECTORS_DICT.items()}
        self.structure_vectors = {
            key: vector+self.structure_vectors['F'] for key, vector in from_other_point.items()}

        # update car posistion
        self.pos += self.structure_vectors['A']
        self.structure_vectors = {
            key: vector-self.structure_vectors['A'] for key, vector in self.structure_vectors.items()}
        

        self.move_car(new_pos, 'F')
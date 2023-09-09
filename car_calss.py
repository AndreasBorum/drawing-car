import pygame
from car_layout import CAR_STRUCTURE_DICT, CAR_STRUCTURE_VECTORS_DICT, L_V, SPECIAL_POINTS
import math


class Car():
    def __init__(self):
        self.pos = (0, 0)
        self.angle = 0
        self.car_points_v = CAR_STRUCTURE_VECTORS_DICT

        self.structure_vectors = CAR_STRUCTURE_VECTORS_DICT

    def draw(self, surface):
        """Draws the car on the surface"""
        self.rect = pygame.draw.polygon(surface, (0, 0, 0), [
                                        value for key, value in self.get_pos_vectors().items() if key not in SPECIAL_POINTS], 2)
        pygame.draw.circle(surface, 'white', self.pos, 2)

    def turn_car(self, turn_angle_, around='A', in_degrees=False):
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


    def move_car(self, new_pos, point='A'):
        """moves car, by moving a car point to new posistion"""
        self.pos = new_pos-self.structure_vectors[point]

    def get_pos_vectors(self):
        """returns vectors for car points relativ to surface"""
        return {key: coords + self.pos for key, coords in self.structure_vectors.items()}

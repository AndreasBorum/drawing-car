import pygame
import copy
from time import sleep
import numpy as np

from helper import draw_arc_with_center, sub_tuple
from math_module import calculate_path as calculate_next_point
import colors


class Path():
    def __init__(self, points, car_objekt):
        self.path_points = points


        self.virtual_car = copy.copy(car_objekt)
        self.virtual_car.move_car(self.path_points[0], 'F')
        
        self.path_elements = []
        self.calculate_path()
        

    def draw(self, surface):
        for element in self.path_elements:
            pygame.draw.circle(surface, colors.medium, element['C'], element['radius']+1, 1)
            draw_arc_with_center(surface, colors.dark, element['C'], element['A'], element['angle_rad'],element['angle_direction'], element['radius'], 2)
        for point in self.path_points:
            pygame.draw.circle(surface, colors.orange, point, 2)
    



    def calculate_path(self):
        accumulated_length =0

        for i, path_point in enumerate(self.path_points[1:]):
            self.path_elements.append(calculate_next_point(self.virtual_car.get_pos_vectors(), path_point))
            self.virtual_car.turn_car_outside_point(self.path_elements[-1]['angle_rad']*self.path_elements[-1]['angle_direction'], self.path_elements[-1]['C'], in_degrees=False)
            accumulated_length += self.path_elements[-1]['arc_lenght']
            self.path_elements[-1]['accumulated_length'] = accumulated_length

        self.lenght_of_path = self.path_elements[-1]['accumulated_length']
        #print(self.lenght_of_path)

            
    def get_pos_on_path(self, uniform_distance):
        distance = uniform_distance*self.lenght_of_path
        for element in self.path_elements:
            if distance <= element['accumulated_length']:
                return self.get_pos_on_path_element(element['accumulated_length']-distance, element)

    def get_pos_on_path_element(self,distance, element):
        angle = (element['angle_deg']-distance/element['arc_lenght']*element['angle_deg'])*element['angle_direction']
        CA=pygame.Vector2(sub_tuple(element['A'], element['C'])).rotate(angle)
        pos = tuple(CA+pygame.Vector2(element['C']))
        direction = [CA.x, CA.y]
        print(pos, CA, direction, distance, angle)
        sleep(0.1)
        return pos, direction, element['angle_direction']
import numpy as np
import pygame
import math
import copy

from car_calss import Car
from math_module import calculate_path as calculate_next_point

class Path():
    def __init__(self, points, car_objekt):
        self.path_points = points


        self.virtual_car = copy.copy(car_objekt)
        self.virtual_car.move_car(self.path_points[0], 'F')
        
        self.path_elements = []
        self.calculate_path()
        

    def draw(self, surface):
        for element in self.path_elements:
            pygame.draw.circle(surface, (0,0,200), element['C'], element['radius'], 1)
            self.draw_arc_with_center(surface, (255,255,255), element['C'], element['A'], element['angle_rad'],element['angle_direction'], element['radius'], 2)
        for point in self.path_points:
            pygame.draw.circle(surface, (255,0,0), point, 2)
    
    def draw_arc_with_center(self, screen, color, center, start_point, angle, angle_direction, radius, thickness):
        C=np.array(center)
        S=np.array(start_point)
        X_axis = np.array([1,0])
        CS=S-C
        #print(angle_direction)

        # makes the rect the circle is in
        rect = pygame.Rect(center[0] - radius, center[1] - radius, 2 * radius, 2 * radius)

        # Calculate the start and end angles based on the given points
        start_angle = -np.arccos(CS.dot(X_axis)/(np.linalg.norm(CS)*np.linalg.norm(X_axis)))
        finish_angle = start_angle + (-angle_direction)*angle

        print(start_angle, finish_angle)
        if angle_direction == 1:
            start_angle ,finish_angle = finish_angle, start_angle

        

        pygame.draw.arc(screen, color, rect, start_angle, finish_angle, thickness)


    def calculate_path(self):
        accumulated_length =0

        for i, path_point in enumerate(self.path_points[1:]):
            self.path_elements.append(calculate_next_point(self.virtual_car.get_pos_vectors(), path_point))
            self.virtual_car.turn_car_outside_point(self.path_elements[-1]['angle_rad']*self.path_elements[-1]['angle_direction'], self.path_elements[-1]['C'], in_degrees=False)
            accumulated_length += self.path_elements[-1]['arc_lenght']
            self.path_elements[-1]['accumulated_length'] = accumulated_length

        self.lenght_of_path = self.path_elements[-1]['accumulated_length']
        #print(self.lenght_of_path)

    # def calculate_next_point(self, car_vectors, target):
    #     A = np.array(car_vectors['F'])
    #     B = np.array(target)
    #     R = np.array(car_vectors['RW'])
    #     L = np.array(car_vectors['LW'])

    #     AB = B-A
    #     M = (AB)/2+A
    #     v = np.array((-AB[1], AB[0]))
    #     LR= R-L


    #     # checks if the lines af parallel 
    #     if np.linalg.det([LR, v]) == 0:
    #         visuals ={'M':tuple(M), 'radius':0}
    #         return M, 0, visuals, 0

    #     # finder skæringspunktet
    #     s = np.cross(LR,(R-M))/np.cross(LR,v)
    #     t = np.cross(v,(M-np.array(car_vectors['centerW'])))/np.cross(v,LR)

    #     new_v = v*s
    #     C=new_v+M

    #     CA = A-C
    #     CB = B-C
    #     angle = np.arccos(CA.dot(CB)/(np.linalg.norm(CA)*np.linalg.norm(CB))) # returns radians
    #     car_direction =1 if np.sign(s)!=np.sign(t) else -1
    #     angle_direction =np.sign(s)
    #     radius = np.linalg.norm(C-A)

    #     arc_lenght= 2*np.pi*radius*angle/360

    #     results ={'A':tuple(A),
    #               'B':tuple(B),
    #               'M':tuple(M), 
    #               'radius':radius,
    #               'C': tuple(C),
    #               'angle_rad': angle,
    #               'angle_deg': math.degrees(angle),
    #               'car_direction': car_direction,
    #               'angle_direction': angle_direction,
    #               'arc_lenght': arc_lenght
    #               }
        
    #     return results
            
    def get_pos_on_path(self, uniform_distance):
        distance = uniform_distance*self.lenght_of_path
        for element in self.path_elements:
            if distance <= element['accumulated_length']:
                return self.get_pos_on_path_element(element['accumulated_length']-distance, element)

    def get_pos_on_path_element(self,distance, element):
        AC = pygame.Vector2(element['A']-element['C'])
        angle = distance/element['arc_lenght']*element['angle']*element['angle_direction']
        AC.rotate_rad(angle)
        return AC+pygame.Vector2(element['C'])
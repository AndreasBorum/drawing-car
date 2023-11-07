import pygame
import numpy as np


def sub_tuple(tuple_1, tulple_2):
    return tuple(map(lambda i, j: i - j, tuple_1, tulple_2))


def draw_arc_with_center(screen, color, center, start_point, angle, angle_direction, radius, thickness):
    '''
    draws an arc with a center and start point
    angle_direction: 1 for clockwise, -1 for counter clockwise
    angle: angle in degrees
    radius: radius of the arc
    thickness: thickness of the arc
    center: center of the arc
    start_point: start point of the arc
    color: color of the arc
    screen: screen to draw on
    returns: nothing
    '''

    # converts to vectors 
    C=np.array(center)
    S=np.array(start_point)
    X_axis = np.array([1,0])
    CS=S-C
    #print(angle_direction)

    # makes the rect the circle is in
    rect = pygame.Rect(center[0] - radius-1, center[1] - radius-1, 2 * radius+1, 2 * radius+1)

    # Calculate the start and end angles based on the given points
    start_angle = np.sign(np.cross(CS,X_axis))*np.arccos(CS.dot(X_axis)/(np.linalg.norm(CS)*np.linalg.norm(X_axis)))
    finish_angle = start_angle - angle*angle_direction

    #print(start_angle, finish_angle)
    if angle_direction == 1:
        start_angle ,finish_angle = finish_angle, start_angle

    

    pygame.draw.arc(screen, color, rect, start_angle, finish_angle, thickness)
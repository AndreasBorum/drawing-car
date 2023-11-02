import pygame
import math

def sub_tuple(tuple_1, tulple_2):
    return tuple(map(lambda i, j: i - j, tuple_1, tulple_2))

def draw_arc_with_center(screen, color, center, start_point, angle, radius, thickness):
    rect = pygame.Rect(center[0] - radius, center[1] - radius, 2 * radius, 2 * radius)

    # Calculate the start and end angles based on the given angle
    start_angle = math.degrees(math.atan2(start_point[1] - center[1], start_point[0] - center[0]))
    end_angle = start_angle + angle

    return pygame.draw.arc(screen, color, rect, math.radians(start_angle), math.radians(end_angle), thickness)
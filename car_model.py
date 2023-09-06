import pygame

CAR_STRUCTUR_DICT = {
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
CAR_STRUCTUR_DICT = {key: tuple(10 * value for value in coords)
                     for key, coords in CAR_STRUCTUR_DICT.items()}

CAR_STRUCTUR_VECTORS_DICT = {key: pygame.math.Vector2(coords)
                     for key, coords in CAR_STRUCTUR_DICT.items()}


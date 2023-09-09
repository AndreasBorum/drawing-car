import pygame

CAR_STRUCTURE_DICT = {
    'A': (0, 0),
    'B': (0, 3),
    'C': (1, 3),
    'D': (1, 2),
    'E': (3, 3),
    'F': (3, 6),
    'G': (4, 3),
    'H': (5, 2),
    'I': (5, 3),
    'J': (6, 3),
    'K': (6, 0),
    'L': (5, 0),
    'M': (5, 1),
    'N': (1, 1),
    'O': (1, 0),
    'center': (3, 2),
    'RW': (5.5, 1.5),
    'LW': (0.5, 1.5),
}
SPECIAL_POINTS = ['center','RW','LW' ]
CAR_STRUCTURE_DICT = {key: tuple(10 * value for value in coords)
                     for key, coords in CAR_STRUCTURE_DICT.items()}

CAR_STRUCTURE_VECTORS_DICT = {key: pygame.math.Vector2(coords)
                     for key, coords in CAR_STRUCTURE_DICT.items()}

R_V = pygame.math.Vector2(tuple(map(lambda x, y: (x - y)/2, CAR_STRUCTURE_VECTORS_DICT['I'], CAR_STRUCTURE_VECTORS_DICT['K'])))
L_V = pygame.math.Vector2(tuple(map(lambda x, y: (x - y)/2, CAR_STRUCTURE_VECTORS_DICT['C'], CAR_STRUCTURE_VECTORS_DICT['A'])))


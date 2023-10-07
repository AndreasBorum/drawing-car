import numpy as np
import math
from pygame import Vector2


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

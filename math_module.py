import numpy as np
import sympy as sp
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
        return (0,0)

    # finder skæringspunktet
    s = np.cross(LR,(R-M))/np.cross(LR,v)

    new_v = v*s
    C=new_v+M

    CA = A-C
    CB = B-C
    angle = np.arccos(CA.dot(CB)/(np.linalg.norm(CA)*np.linalg.norm(CB)))

    visuals ={'M':tuple(M), 'radius':np.linalg.norm(C-A)}

    return tuple(C), angle, visuals


def car_step(C, R,L, angle,current_angle,speed):
    speed *= math.copysign(1,angle)

    angle_to_next= angle-current_angle
    if abs(speed)>abs(angle_to_next):
        speed=angle_to_next
        new_current_angle = 0
    else:
        new_current_angle = current_angle+speed
    
    new_L = (Vector2(L)-Vector2(C)).rotate_rad(-speed)-(Vector2(L)-Vector2(C))+L
    new_R = (Vector2(R)-Vector2(C)).rotate_rad(-speed)-(Vector2(R)-Vector2(C))+R

    print(f'car step func-  full angle:{round(angle, 6)}  speed:{round(speed,6)}  new_current_angle:{round(new_current_angle,6)} ')
    print(f"   Centrum:{C}   before- R:{R}  L:{L}      after- R:{new_R}  L:{new_L}")
    return new_R, new_L, new_current_angle
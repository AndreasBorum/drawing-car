import numpy as np
import sympy as sp
from pygame import Vector2


def find_intersect(start_, end_, l_wheel_, r_wheel_):
    A = np.array(start_)
    B = np.array(end_)
    R = np.array(r_wheel_)
    L = np.array(l_wheel_)
    #print(A,B,R,L)

    AB = B-A
    M = (AB)/2+A
    v = np.array((-AB[1], AB[0]))
    LR= R-L


    # checks if the lines af parallel 
    if np.linalg.det([LR, v]) == 0:
        return None
    

    # finder skæringspunktet
    s, t = sp.symbols('s t')
    equation1 = sp.Eq(LR[0]*t+L[0], v[0]*s+M[0])
    equation2 = sp.Eq(LR[1]*t+L[1], v[1]*s+M[1])
    solution = sp.solve((equation1, equation2), (s, t))
    #print(solution)
    
    new_v = np.array([v[0]*solution[s], v[1]*solution[s]], dtype=float)
    new_LR = np.array([LR[0]*solution[t], LR[1]*solution[t]], dtype=float)
    intersect=new_v+M
    #print('new between, wheels', new_v, new_LR)



    lenghts= [np.linalg.norm(intersect-point) for point in (A,L,R)]
    #print('inter, len: ',intersect, lenghts)

    angle = np.arccos(new_v.dot(new_LR)/(np.linalg.norm(new_v)*np.linalg.norm(new_LR)))
    print('Angle: ', angle)

    lenght_to_next = angle*lenghts[0]
    
    #print('lenght to next point', lenght_to_next)
    #print('CL:', -new_LR)
    return tuple(intersect), angle

def car_step(C, R,L, angle,current_angle,speed):

    angle_to_next= angle-current_angle
    if speed>angle_to_next:
        speed=angle_to_next
        new_current_angle = 0
    else:
        new_current_angle = current_angle+speed
    
    new_L = (Vector2(L)-Vector2(C)).rotate_rad(-speed)-(Vector2(L)-Vector2(C))+L
    new_R = (Vector2(R)-Vector2(C)).rotate_rad(-speed)-(Vector2(R)-Vector2(C))+R

    print(f'car step func-  full angle:{round(angle, 6)}  speed:{round(speed,6)}  new_current_angle:{round(new_current_angle,6)} ')
    print(f"   Centrum:{C}   before- R:{R}  L:{L}      after- R:{new_R}  L:{new_L}")
    return new_R, new_L, new_current_angle
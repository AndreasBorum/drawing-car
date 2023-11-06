import numpy as np
import math

def calculate_path(car_vectors, target):
    A = np.array(car_vectors['F'])
    B = np.array(target)
    R = np.array(car_vectors['RW'])
    L = np.array(car_vectors['LW'])

    AB = B-A
    M = (AB)/2+A
    v = np.array((-AB[1], AB[0]))
    LR= R-L


    # The following code is intended to handle cases where the determinant is zero,
    # ensuring that the code behaves correctly when LR and v are parallel.
    if np.linalg.det([LR, v]) == 0:
        LR +=np.array([0.1,0.1])

    # finder skæringspunktet
    s = np.cross(LR,(R-M))/np.cross(LR,v)
    t = np.cross(v,(M-np.array(car_vectors['centerW'])))/np.cross(v,LR)

    new_v = v*s
    C=new_v+M

    CA = A-C
    CB = B-C
    angle = np.arccos(CA.dot(CB)/(np.linalg.norm(CA)*np.linalg.norm(CB))) # returns radians
    car_direction =1 if np.sign(s)!=np.sign(t) else -1
    angle_direction =np.sign(s)
    radius = np.linalg.norm(C-A)

    arc_lenght= 2*np.pi*radius*angle/360

    results ={'A':tuple(A),
                'B':tuple(B),
                'M':tuple(M), 
                'radius':radius,
                'C': tuple(C),
                'angle_rad': angle,
                'angle_deg': math.degrees(angle),
                'car_direction': car_direction,
                'angle_direction': angle_direction,
                'arc_lenght': arc_lenght
                }
    
    return results
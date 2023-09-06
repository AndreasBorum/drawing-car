import numpy as np
import sympy as sp


def find_intersect(start_, end_, l_wheel_, r_wheel_):
    start = np.array(start_)
    end = np.array(end_)
    r_wheel = np.array(r_wheel_)
    l_wheel = np.array(l_wheel_)
    print(start,end,r_wheel,l_wheel)

    start_end_v = end-start
    between = (start_end_v)/2+start
    between_v = np.array((-start_end_v[1], start_end_v[0]))
    between_wheels_v = r_wheel-l_wheel

    wheel_v = r_wheel-l_wheel
    print('Between vector: ',start_end_v)
    print('Between point: ',between)
    print('Between 90 vector: ',between_v)
    print('Between wheels: ',between_wheels_v)

    # checks if the lines af parallel 
    if np.linalg.det([wheel_v, between_v]) == 0:
        return None
    

    # finder skæringspunktet
    s, t = sp.symbols('s t')
    equation1 = sp.Eq(between_wheels_v[0]*t+l_wheel[0], between_v[0]*s+between[0])
    equation2 = sp.Eq(between_wheels_v[1]*t+l_wheel[1], between_v[1]*s+between[1])
    solution = sp.solve((equation1, equation2), (s, t))
    print(solution)
    new_between_v = np.array([between_v[0]*solution[s], between_v[1]*solution[s]], dtype=float)
    new_between_wheels_v = np.array([between_wheels_v[0]*solution[t], between_wheels_v[1]*solution[t]], dtype=float)
    intersect=new_between_v+between
    print('new between, wheels', new_between_v, new_between_wheels_v)

    lenght= np.linalg.norm(intersect-l_wheel)
    print('inter, len: ',intersect, lenght)
    return tuple(intersect), lenght

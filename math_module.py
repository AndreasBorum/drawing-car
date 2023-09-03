import random
import numpy as np


def line_between(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    z = 0

    if y1 == y2:
        y2 += 0.001
    if x1 == x2:
        a2 = 0
    else:
        a1 = (y1-y2)/(x1-x2)

        a2 = -1/a1
    x3, y3 = ((x2-x1)/2+x1), ((y2-y1)/2+y1)
    b = y3-a2*x3

    return (a2, b)


def wheels_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        x2 += 0.001

    if y1 == y2:
        a = 0
    else:
        a = (y1-y2)/(x1-x2)

    b = y1-a*x1

    return (a, b)


def point_intersect(line1, line2):
    a1, b1 = line1
    a2, b2 = line2
    if a1 == a2:
        a1 += 0.001

    x = (b2-b1)/(a1-a2)
    y = a1*x+b1

    return (x, y)


def angle(p1, p2, c):

    def angle_between(v1, v2):
        """ Returns the angle in radians between vectors 'v1' and 'v2'::
        """
        def unit_vector(vector):
            """ Returns the unit vector of the vector.  """
            return vector / np.linalg.norm(vector)

        v1_u = unit_vector(v1)
        v2_u = unit_vector(v2)
        print("normalvektorer:", v1_u, v2_u)
        return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

    c_p1 = np.subtract(p1, c)
    c_p2 = np.subtract(p2, c)
    return angle_between(c_p1, c_p2)


def wrapper(p_start, p_end, r_wheel, l_wheel):
    b_line = line_between(p_start, p_end)
    print("b_line: ", b_line)
    w_line = wheels_line(r_wheel, l_wheel)
    print("w_line: ", w_line)
    center = point_intersect(b_line, w_line)
    print("center: ", center)
    v = angle(p_start, p_end, center)
    print("angle: ", np.degrees(v))


wrapper((0, 3), (0, -5), (1, 0), (-1, 0))
# for _ in range(100):

#     wrapper((random.randint(1, 100), random.randint(1, 100)), (random.randint(1, 100), random.randint(
#         1, 100)), (random.randint(1, 100), random.randint(1, 100)), (random.randint(1, 100), random.randint(1, 100)))

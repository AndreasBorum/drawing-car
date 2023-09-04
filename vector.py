import numpy as np
import sympy as sp


def find_angel(start, end, r_wheel, l_wheel):
    between = (end-start)/2+start
    start_end_v = end-start
    between_v = np.array((-start_end_v[1], start_end_v[0]))

    wheel_v = r_wheel-l_wheel
    print(between_v)

    # checks if the lines af parallel 
    if np.linalg.det([wheel_v, between_v]) == 0:
        print("check")
        return None
    

    # finder skæringspunktet
    s, t = sp.symbols('s t')
    equation1 = sp.Eq(wheel_v[0]*t+r_wheel[0], between_v[0]*s+between[0])
    equation2 = sp.Eq(wheel_v[1]*t+r_wheel[1], between_v[1]*s+between[1])
    solution = sp.solve((equation1, equation2), (s, t))
    intersect = np.array([solution[s], solution[t]], dtype=float)

    print(intersect)


start = np.array([0, 4])
end = np.array([1, 5])
r_wheel = np.array([1, 0])
l_wheel = np.array([-1, 0])



def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        find_angel(start, end, r_wheel, l_wheel)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats(50)
    #stats.dump_stats(filename='needs_profiling.prof')


if __name__ == '__main__':
    main()
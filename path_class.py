import numpy as np  #used for vectors and other math
import sympy as sp  #used for solving equations

class path():
    def __init__(self, car_vectors, target) -> None:
        self.car_vectors = car_vectors
        self.A = np.array(car_vectors['F'])
        self.B = np.array(target)
        self.R = np.array(car_vectors['RW'])
        self.L = np.array(car_vectors['LW'])

        self.AB = self.B-self.A
        self.M = (self.AB)/2+self.A
        self.v = np.array((-self.AB[1], self.AB[0]))
        self.LR= self.R-self.L


        # checks if the lines af parallel 
        if np.linalg.det([self.LR, self.v]) == 0:
            self.movement_type = 'straight'
            self.target_car_vectors = {key: coords + self.AB for key, coords in self.car_vectors.items()}
        else:
            # finder skæringspunktet
            s, t = sp.symbols('s t')
            equation1 = sp.Eq(self.LR[0]*t+self.L[0], self.v[0]*s+self.M[0])
            equation2 = sp.Eq(self.LR[1]*t+self.L[1], self.v[1]*s+self.M[1])
            solution = sp.solve((equation1, equation2), (s, t))

            new_v = np.array([self.v[0]*solution[s], self.v[1]*solution[s]], dtype=float)
            new_LR = np.array([self.LR[0]*solution[t], self.LR[1]*solution[t]], dtype=float)
            self.C=new_v+self.M
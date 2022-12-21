###### Description ######
# This is a culmination of math numerical methods written by me #
#########################################
#########################################


########## Imports ############
import numpy as np
import matplotlib.pyplot as plt
###############################
###############################


class funMath:

    def __init__(self):
        """
        A variety of math methods        
        """

        pass

    
    
    def Secant(func, int, p0, p1, tol, n):
        """
        INPUTS:
            - func      :   The function to solve (i.e. f(x) = 0, f --> func)
            - int       :   The interval over which to solve the problem (i.e. (-1,1)).
            - p0        :   First guess for the zero
            - p1        :   Second guess for the zero
            - tol       :   The tolerance for which to solve the problem
            - n         :   Number of iterations to run before code breaks

        OUTPUT:
            - Approximation for the solution to the problem given the tolerance
        """
        Ps = [p0,p1]     # Define a list to fill with p values
        i = 0            # Number of iterations that have been ran
        while True:
            i += 1
            # Create next term in series
            p = Ps[-1] -  (  (Ps[-1]-Ps[-2]) * func(Ps[-1])  ) / (func(Ps[-1])  -  func(Ps[-2]))

            if np.abs(p-Ps[-1]) < tol:
                # If within acceptable tolerance, return approx:
                print(f"Approximate zero value on interval [{int[0]},{int[1]}] found at x = {p} in {len(Ps)+1}-steps")
                break

            elif i >= n:
                print("Maximum iterations reached!")
                print(f"Approximate zero value on interval [{int[0]},{int[1]}] found at x = {p}")
                print("Higher iteration count may be needed for given tolerance!")
                break
            
            else:
                Ps.append(p)

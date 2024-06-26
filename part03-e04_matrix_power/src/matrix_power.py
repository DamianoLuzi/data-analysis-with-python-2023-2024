#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0], dtype = int)
    else:
        gen = (a for i in range(abs(n)))
        fun = lambda x,y : x@y
        a_power_n = reduce(fun, gen)
        if n > 0:
            return a_power_n 
        else:
            return np.linalg.inv(a_power_n)

        


    

def main():
    a = np.array([[0,1], [-1,0]])
    print(matrix_power(a, -3))
    return

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    length = X.shape[0]
    print(length)
    res = np.zeros((length))
    
    for i in range(length):
        res[i] = (np.dot(X[i], Y[i])/scipy.linalg.norm(X[i])/scipy.linalg.norm(Y[i]))
        print(res[i])

    print(f"res: {res}")
    clipped = np.clip(res, -1, 1)
    print(f"clipped: {clipped}")
    angles = np.arccos(clipped)
    return np.degrees(angles)

def main():
    v = np.array([[0,0,1],[-1,1,0]])
    w = np.array([[0,1,0], [1,1,0]])
    print(vector_angles(v, w))

if __name__ == "__main__":
    main()

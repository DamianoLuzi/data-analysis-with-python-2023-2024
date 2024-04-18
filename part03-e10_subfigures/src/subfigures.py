#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, ax = plt.subplots(1,2)
    ax[0].plot(a[:,0], a[:,1])
    ax[1].scatter(a[:,0], a[:,1], s=a[:,3],c=a[:,2]) #c -> color based on a's 3rd column
                                                      #s -> size based on a's 4th column
    plt.show()

def main():
    a = np.array([[1,3,5,3], [3,1,5,3], [4,6,8,3], [0,0,5,5]])
    subfigures(a)

if __name__ == "__main__":
    main()

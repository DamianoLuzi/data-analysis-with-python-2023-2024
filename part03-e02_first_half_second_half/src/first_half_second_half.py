#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m = int (a.shape[1]/2)
    fhs = np.sum(a[:,:m],1)
    shs = np.sum(a[:,m:],1)
    return a[fhs > shs]

def main():
    pass

if __name__ == "__main__":
    main()

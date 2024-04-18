#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    """ res = []
    print(a[:,2])
    for i in range(0,len(a)):
        print(i, a[i][1], a[i][-2])
        if a[i][1] > a[i][-2]:
            res.append(a[i])
    print(res) """
    b = a[:,-2] < a[:,1]
    return a[b]
    
def main():
    column_comparison(
       [[8, 9, 3, 8, 8],
         [0, 5, 3, 9, 9],
           [5, 7 ,6, 0, 4],
             [7,8,1 ,6, 2],
 [2,1 ,3, 5, 8]]
 )
    pass

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def interleave(*lists):
    res=[]
    aux = []
    for x in lists:
        aux.append(x)
    z = list(zip(*aux))
    for l in z:
        for j in l:
            res.append(j)    
    return res

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()

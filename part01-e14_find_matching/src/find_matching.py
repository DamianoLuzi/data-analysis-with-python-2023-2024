#!/usr/bin/env python3

def find_matching(L, pattern):
    res=[]
    for i,j in enumerate(L):
        if(pattern in j):
            res.append(i)
        print(i,j)
    return res

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")

if __name__ == "__main__":
    main()

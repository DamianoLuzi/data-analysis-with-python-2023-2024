#!/usr/bin/env python3

def merge(L1, L2):
    merged= []
    i,j = 0,0
    while i<len(L1) and j<len(L2):
        if L1[i] > L2[j]:
            merged.append(L2[j])
            j+=1
        else:
            merged.append(L1[i])
            i+=1
    merged = merged + L1[i:] + L2[j:]
    return merged

def main():
    L1 = [1,3,9,12]
    L2 = [2,5,10]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()

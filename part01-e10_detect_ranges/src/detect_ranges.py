#!/usr/bin/env python3

def detect_ranges(L):
    sl = sorted(L)
    rstart=0
    rend=0
    ranges=[]
    for i in range(1, len(sl)):
        if sl[i-1] == sl[i]-1:
            rend=i
            if i == len(sl)-1:
                ranges.append((sl[rstart],sl[rend]+1))
        else:
            if rstart == rend:
                ranges.append(sl[rstart])
            else:
                ranges.append((sl[rstart], sl[rend]+1))
            rstart=rend=i
            if i == len(sl)-1:
                ranges.append(sl[-1])


    return ranges

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

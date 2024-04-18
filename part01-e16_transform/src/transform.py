#!/usr/bin/env python3

def transform(s1, s2):
    l1 = s1.split()
    l2 = s2.split()
    il1 = list(map(lambda x : int(x), l1))
    il2 = list(map(lambda x: int(x),l2))
    zip(il1,il2)
    return list(map(lambda x,y : x*y, il1, il2))

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()

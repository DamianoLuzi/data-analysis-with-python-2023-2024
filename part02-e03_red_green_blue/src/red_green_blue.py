#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    res = []
    f = open(filename,"r+")
    next(f)
    expression= r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)'#r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)'
    for i in f:
        print(i)
        fields = re.split(r'\s+',i)
        print(fields)
        r,g,b,name = re.search(expression, i).groups()
        print(r,g,b,name)
        res.append("\t".join([r,g,b,name]))
    return res


def main():
    red_green_blue()
    pass

if __name__ == "__main__":
    main()

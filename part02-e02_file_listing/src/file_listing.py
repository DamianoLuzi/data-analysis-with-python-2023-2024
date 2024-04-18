#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    f = open(filename,"r+")
    res=[]
    expression=r'(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s(.+)'
    #              sz sp  mnt  sp day sp   hr : min sp
    for line in f:
        #print(line)
        fields = re.split(r'\s+',line)
        print(fields)
        size, month, day, hour, minute, filename = re.search(expression, line).groups()
        res.append((int(size), month, int(day), int(hour), int(minute), filename))
    return res

def main():
    file_listing()

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import sys

def file_count(filename):
    f = open(filename, "r+")
    lc = 0
    wc = 0
    cc = 0
    for line in f:
        lc += 1
        splitted = line.split()
        wc += len(splitted)
        cc += len(line)
    return (lc, wc, cc)

def main():
    files = sys.argv[1:]
    for f in files:
        l,w,c = file_count(f)
        print(f'{l}\t{w}\t{c}\t{f}')
    pass

if __name__ == "__main__":
    main()

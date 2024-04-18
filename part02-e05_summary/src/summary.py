#!/usr/bin/env python3

import sys
import statistics

def summary(filename):
    #print("summary executed")
    f = open(filename,"r+")
    nums=[]
    for line in f:
        try:
            nums.append(float(line))
        except: pass
    #print("nums",nums)
    s = sum(nums)
    a= statistics.mean(nums)
    sdev = statistics.stdev(nums)

    return (s,a,sdev)

def main():
    files = sys.argv[1:]
    #print("files ",files)
    for f in files:
        sum ,avg, stdev = summary(f)
        print(f"File: {f} Sum: {sum:.6f} Average: {avg:.6f} Stddev: {stdev:.6f}")
    

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def distinct_characters(L):
    dc = dict()
    for string in L:
        chars = set(string)
        dc[string] = len(chars)
    return dc

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()

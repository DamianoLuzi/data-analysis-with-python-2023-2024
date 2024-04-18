#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    s = ""
    def __init__(self,str):
        self.s = str
    def write(self,string):
        print(self.s+string)


def main():
    p = Prepend("+++ ")
    p.write("Hello")
    pass

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0: return "0 = 0"
    else:
        Lsum = sum(L)
        s = [str(x) for x in L]
        return ' + '.join(s)+' = '+str(Lsum)

def main():
    sum_equation([1,5,7])

if __name__ == "__main__":
    main()

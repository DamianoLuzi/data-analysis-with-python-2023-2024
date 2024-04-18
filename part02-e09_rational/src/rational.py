#!/usr/bin/env python3

class Rational(object):
    def __init__(self, a,b):
        self.num = a
        self.den = b
    def __str__(self):
        return f'{self.num}/{self.den}'
    def __add__(self, n):
        gcd = int(self.den) * int(n.den)
        x = gcd / self.den
        y = gcd / n.den
        new_num = int(x*int(self.num) + y*int(n.num))
        return Rational(new_num, gcd)
    def __sub__(self, numb):
        new_denom = int(self.den) * int(numb.den)
        mult1 = new_denom / self.den
        mult2 = new_denom / numb.den
        new_nume = int(mult1 * int(self.num) - mult2 * int(numb.num))
        return Rational(new_nume, new_denom)

    def __mul__(self, numb):
        #multiplication
        new_denom = int(self.den * numb.den)
        new_nume = int(self.num * numb.num)
        return Rational(new_nume, new_denom)

    def __truediv__(self, numb):
        new_nume = int(self.num * numb.den)
        new_denom = int(self.den * numb.num)
        return Rational(new_nume, new_denom)

    def __eq__(self, numb):
        return self.num == numb.num and self.den == numb.den

    def __gt__(self, numb):
        new_denom = int(self.den) * int(numb.den)
        mult1 = new_denom / self.den
        mult2 = new_denom / numb.den
        return mult1 * self.num > mult2 * self.den

    def __lt__(self, numb):
        new_denom = int(self.den) * int(numb.den)
        mult1 = new_denom / self.den
        mult2 = new_denom / numb.den
        return mult1 * self.num < mult2 * self.den
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()

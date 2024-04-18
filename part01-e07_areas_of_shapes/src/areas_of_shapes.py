 #!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        shape=input("Choose a shape (triangle, rectangle, circle):")
        if shape=="": break
        elif shape =="triangle":
            base=input("Give base of the triangle:")
            height=input("Give height of the triangle:")
            print("The area is "+ str(int(base)*int(height)/2))
        elif shape =="circle":
            radius=input("Give radius of the circle:")
            print("The area is "+ str(int(radius)**2*math.pi))
        elif shape=="rectangle":
            w=input("Give width of the rectangle:")
            h=input("Give height of the rectangle:")
            print("The area is "+ str(int(w)*int(h)))
        else: print("Unknown shape!")



if __name__ == "__main__":
    main()

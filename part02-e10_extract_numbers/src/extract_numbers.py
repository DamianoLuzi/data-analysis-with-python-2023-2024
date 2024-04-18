#!/usr/bin/env python3

def extract_numbers(s):
    words = s.split()
    res=[]
    n = 0
    for w in words:
        print(w)
        try:
            res.append(int(w))
        except:
            try:
                res.append(float(w))
            except:
                print("cannot convert string")
        
    return res

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()

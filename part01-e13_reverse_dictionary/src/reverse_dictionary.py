#!/usr/bin/env python3

def reverse_dictionary(d):
    rev = {}
    for key in d:
        print("key",key)
        for value in d[key]:
            print("value",value)
            if value in rev:
                rev[value].append(key)
            else:
                rev[value] = [key]
        print(rev)
    return rev


def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    rev = reverse_dictionary(d)
    print(rev)
    

if __name__ == "__main__":
    main()

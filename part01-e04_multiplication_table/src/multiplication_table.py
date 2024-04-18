#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            result = str(i * j)
            print(result.rjust(4), end=' ')
        print("")

if __name__ == "__main__":
    main()

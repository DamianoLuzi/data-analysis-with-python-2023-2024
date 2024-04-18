#!/usr/bin/env python3
import pandas as pd

def read_series():
    values = []
    indexes = []
    while True:
        data = input("input:")
        if len(data) == 0:
            break
        else:
            s = data.split()

            if len(s) < 2:
                raise Exception
            else:
                indexes.append(s[0])
                values.append(s[1])
    return pd.Series(values, indexes)

def main():
    read_series()
    pass

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv('src/municipal.tsv',sep='\t')
    shape = df.shape
    print(f"Shape: {shape[0]},{df.shape[1]}")
    print("Columns:")
    for i in df.columns:
        print(i)
    return


if __name__ == "__main__":
    main()

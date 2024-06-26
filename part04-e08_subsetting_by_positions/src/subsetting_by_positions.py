#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep = '\t', index_col = 0)
    return df.iloc[:10][['Title', 'Artist']] #:10 top 10 - [] : selecting a list of columns

def main():
    subsetting_by_positions()

if __name__ == "__main__":
    main()

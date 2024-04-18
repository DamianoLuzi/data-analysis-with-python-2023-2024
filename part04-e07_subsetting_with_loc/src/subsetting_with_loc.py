#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col = 0)
    cols = df.columns
    #selecting rows with slicing - selecting a list of columns with []
    return df.loc['Akaa':'Äänekoski'][[cols[0], cols[2], cols[3]]]
    return None

def main():
    print(subsetting_with_loc())

if __name__ == "__main__":
    main()

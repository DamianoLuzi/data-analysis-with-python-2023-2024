#!C:\Python311\python.exe

import pandas as pd

def top_bands():
    top = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    bands = pd.read_csv('src/bands.tsv', sep='\t')
    print(top)
    print(bands)
    #converting band names to all upper case
    bands['Band'] = bands['Band'].str.upper()
    print(bands)
    merged = pd.merge(top, bands, left_on=['Artist'], right_on=['Band'])
    print(merged.loc[:,'Band'])
    print(merged.loc[:,'Artist'])
    print(merged.loc[1,:])
    return merged

def main():
    top_bands()

if __name__ == "__main__":
    main()

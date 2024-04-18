#!C:\Python311\python.exe

import pandas as pd

def best_record_company():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep="\t")
    #grouping by publisher
    groups = df.groupby('Publisher')
    #associating the sum of the WoC related to a specififc publisher
    a = groups['WoC'].sum()
    #sorting 
    a = a.sort_values(ascending=False)
    print(a.index)
    top = a.index[0]
    print(a)
    #merging with conditional accessing
    #aimimng to return the subset where the publisher is the top publisher
    res = df[df.Publisher == top]
    print("res", res)
    return res

def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()

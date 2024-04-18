#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=";")
    df.head()
    drop_rows = df.dropna(how='all')# removing empty rows
    drop_cols = drop_rows.dropna(axis = 1, how = 'all')#removing empty cols from df with dropped rows
    return drop_cols


def main():
    print(cyclists())
    return
    
if __name__ == "__main__":
    main()

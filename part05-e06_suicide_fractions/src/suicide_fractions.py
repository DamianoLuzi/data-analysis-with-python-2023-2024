#!C:\Python311\python.exe

import pandas as pd

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv')
    #suicide ratio
    df['suicide_ratio'] = df['suicides_no']/df['population']
    print(df)
    #grouping by country
    res = df.groupby('country')
    res = res['suicide_ratio'].mean()
    return res
def main():
    suicide_fractions()
    return

if __name__ == "__main__":
    main()

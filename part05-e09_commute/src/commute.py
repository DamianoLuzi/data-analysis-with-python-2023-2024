#!C:\Python311\python.exe

import pandas as pd
import matplotlib.pyplot as plt

def split_date_continues():
    df = pd.read_csv('src/file.csv',sep=";")
    print(df)
    df = df.dropna(how='all')
    df = df.dropna(axis = 1,how='all')
    print(df)
    #retrieving all rows from first column
    col = df.iloc[:,0]
    df = df.drop(df.columns[0], axis = 1)
    col = col.str.split(expand=True)
    print("col", col)
    col.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    print("col", col)
    col["Hour"] = col["Hour"].str[0:2]

    weekdays = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun"
    }

    months = {
        "tammi": 1,
        "helmi": 2,
        "maalis": 3,
        "huhti": 4,
        "touko": 5,
        "kesä": 6,
        "heinä": 7,
        "elo": 8,
        "syys": 9,
        "loka": 10,
        "marras": 11,
        "joulu": 12,
    }

    col["Weekday"] = col["Weekday"].map(weekdays)
    col["Month"] = col["Month"].map(months)
    col = col.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    res = pd.concat([col, df], axis=1)
    print(res)
    return res

def bicycle_timeseries():
    df = split_date_continues()
    df["Date"] = pd.to_datetime(df[["Day", "Month", "Year", 'Hour']], dayfirst=True)
    df = df.drop(['Day', 'Month', 'Year', 'Hour', 'Weekday'], axis=1)
    df = df.set_index("Date")
    return df

def commute():
    #alternatively
    #df = split_date_continues()
    
    #df = df[(df['Month'] == 8) & (df['Year'] == 2017)]
    df = bicycle_timeseries()
    df = df["2017-08-01":"2017-08-31"]
    print("df",df)
    df['Weekday'] = df.index.weekday
    df['Weekday'] = df['Weekday'] + 1
    df = df.groupby('Weekday').sum()
    print("df",df)
    return df
    
def main():
    df = commute()
    plt.plot(df)
    plt.show()


if __name__ == "__main__":
    main()

#!C:\Python311\python.exe

import pandas as pd
import matplotlib.pyplot as plt


def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=";")
    #dropping empty columns and rows
    df = df.dropna(how="all")
    df = df.dropna(axis = 1, how = 'all')
    print(df)
    groups = df.groupby('Päivämäärä')
    #retrieving first column to then split it
    col = df.iloc[:,0] # : -> all rows, 0 -> first column
    df = df.drop(df.columns[0], axis = 1)

    #splitting first column
    col = col.str.split(expand=True)
    col.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    col['Hour'] = col['Hour'].str[0:2]  #selecting only the fiirst 2 chars of the hour

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

    # mapping <-> translating

    col['Weekday'] = col['Weekday'].map(weekdays)
    col['Month'] = col['Month'].map(months)
    #dictionary with all the column name -> type associations
    col = col.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    #joining dataframes back together
    #axis = 1 because the dataframes need to be joined along the columns axis
    #that is, side to side, rather than on top of each other
    res = pd.concat([col, df], axis=1) 


    return res

def cyclists_per_day():
    df = split_date_continues()
    print(df)
    #removing columns
    df = df.drop(['Hour', 'Weekday'], axis=1)
    print(df)

    res = df.groupby(['Year', 'Month', 'Day']).sum()
    return res
    
def main():
    df = cyclists_per_day()
    df_plot = df.loc[(2017, 8), :]
    plt.plot(df_plot)
    plt.show()

if __name__ == "__main__":
    main()

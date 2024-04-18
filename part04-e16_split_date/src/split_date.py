#!/usr/bin/env python3

import pandas as pd
import numpy as np


""" def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=";")
    df = df.dropna(how = "all") #removing empty rows
    df = df.dropna(axis = 1, how = "all") #removing empty columns
    df = df.iloc[:,0] #selecting all rows form first column
    df = df.str.split(expand= True)
    df.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    df['Hour'] = df['Hour'].str[0:2]
    weekdays = {
        "ma":"Mon",
        "ti":"Tue",
        "ke":"Wed",
        "to":"Thu",
        "pe":"Fri",
        "la":"Sat",
        "su":"Sun"
    }
    
    months = {
        "tammi" :1,
        "helmi" :2,
        "maalis" :3,
        "huhti" :4,
        "touko" :5,
        "kesä":6,
        "heinä" :7,
        "elo" :8,
        "syys" :9,
        "loka" :10,
        "marras" :11,
        "joulu" :12,
    }

    df = df.replace(weekdays, value = None)
    df = df.replace(months, value = None)
    #selecting all rows and columns starting from the second one
    #to convert them into ints
    #and to assign the converted values in the right part of the dataframe
    df.iloc[:,1:] = df.iloc[:,1:].astype(int) 
    return(df) """
def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=";")
    df = df.dropna(how="all").dropna(axis=1, how="all")
    
    # Split the 'Päivämäärä' column into separate columns
    df[['Weekday', 'Day', 'Month', 'Year', 'Hour']] = df['Päivämäärä'].str.split(expand=True)
    
    # Convert 'Weekday' column according to the provided mapping
    weekdays_mapping = {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'}
    df['Weekday'] = df['Weekday'].map(weekdays_mapping)
    
    # Convert 'Month' column according to the provided mapping
    months_mapping = {'tammi': 1, 'helmi': 2, 'maalis': 3, 'huhti': 4, 'touko': 5, 'kesä': 6, 'heinä': 7, 'elo': 8, 'syys': 9, 'loka': 10, 'marras': 11, 'joulu': 12}
    df['Month'] = df['Month'].map(months_mapping)
    
    # Convert 'Hour' column to remove minutes
    df['Hour'] = df['Hour'].str.split(':').str[0]
    
    # Convert columns to appropriate data types
    df[['Day', 'Year', 'Hour']] = df[['Day', 'Year', 'Hour']].astype(int)
    
    return df[['Weekday', 'Day', 'Month', 'Year', 'Hour']]


def main():
    print(split_date())

       
if __name__ == "__main__":
    main()

#!C:\Python311\python.exe

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    print(df)
    x = df.loc[:,'X1':'X5'] # accessing all rows and column from x1 to x5
    y = df.loc[:,'Y'] # accessing all rows from the y column
    model = LinearRegression(fit_intercept=False)
    model.fit(x,y)
    return model.coef_ #weights assigned to each feature to fit the curve

def main():
    coefficients = mystery_data()
    # print the coefficients here
    for i in range(len(coefficients)):
        print(f"Coefficient of X{i+1} is {coefficients[i]}")
    
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    print(df)
    x = df.loc[:,'X1':'X5'] # accessing all rows and column from x1 to x5
    y = df.loc[:,'Y'] # accessing all rows from the y column
    model = LinearRegression(fit_intercept=True)
    model.fit(x,y)
    score = model.score(x,y)  # evaluates the quality of predictions
    print(score)
    rtr = [score]

    for i in range(len(x.columns)):
        #accessing all rows from i-th column
        # in order to reshape them into a matrix
        # -1 -> infer number of rows based on original, 1 -> number of columns
        a = x.iloc[:, i].values.reshape(-1,1)
        #for every column we try to fit it through the model
        model.fit(a,y)
        #we add the score of such prediction to the rtr array
        #that is -> coefficient of determination
        rtr.append(model.score(a,y))
    return rtr
    
def main():
    x = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {x[0]}")
    for i in range(1, len(x)):
        print(f"R2-score with feature(s) X{i}: {x[i]}")

if __name__ == "__main__":
    main()

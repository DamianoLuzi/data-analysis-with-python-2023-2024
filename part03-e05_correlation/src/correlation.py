#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    sepal_len = data[:,0]
    petal_len = data[:,2]
    return (scipy.stats.pearsonr(sepal_len, petal_len)[0])

def correlations():
    data = load()
    m = np.corrcoef(data, rowvar= False)
    return (m)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()

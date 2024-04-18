#!/usr/bin/env python3

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split

def blob_classification(X, y):
    #X -> 2 dimensional array representiong explanatory variables -> features
    #y -> 1 dimensional array represneting the dependent variable

    model = GaussianNB()
    #splitting data
    xtrain, xtest, ytrain, ytest = train_test_split(X,y,random_state=0,train_size=0.75)
    #fitting training data
    model.fit(xtrain, ytrain)
    #testing 
    yt = model.predict(xtest)
    #evaluating prediction quality
    score = metrics.accuracy_score(yt, ytest)
    return score

def main():
    X,y = datasets.make_blobs(100, 2, centers=2, random_state=2, cluster_std=2.5)
    print("The accuracy score is", blob_classification(X, y))
    a=np.array([[2, 2, 0, 2.5],
                [2, 3, 1, 1.5],
                [2, 2, 6, 3.5],
                [2, 2, 3, 1.2],
                [2, 4, 4, 2.7]])
    accs=[]
    for row in a:
        X,y = datasets.make_blobs(100, int(row[0]), centers=int(row[1]),
                                  random_state=int(row[2]), cluster_std=row[3])
        accs.append(blob_classification(X, y))
    print(repr(np.hstack([a, np.array(accs)[:,np.newaxis]])))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy

def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df = pd.read_csv('src/data.tsv', sep="\t")
    #retrieving features from dataframe
    #all rows from X1 and X2 columns
    features = df.loc[:,['X1','X2']]
    #retrieving targets
    #all rows from last column
    labels = df.loc[:,'y']
    lab_len = len(set(labels))
    res = []
    for i in np.arange(0.05, 0.2, 0.05):
        #creating a model with different values of eps
        model = DBSCAN(eps = i)
        # training
        model.fit(features)
        outliers = 0
        clusters = len(set(model.labels_))
        #DBSCAN uses the -1 label to denote outliers
        if -1 in model.labels_:
            clusters -= 1
            #counting the number of occurrences of the -1 label
            #since it represents the number of outliers
            outliers = list(model.labels_).count(-1)
        #aligning infered labels with true labels
        permutation = find_permutation(clusters, labels, model.labels_)
        new_labels = pd.DataFrame([permutation[label] for label in model.labels_]).iloc[:, 0]
        non_outliers_mask = model.labels_ == -1

        if lab_len != clusters:
            score = None
        else:
            #evaluating decision quality through the accuracy_score function
            #passing the labels which are not outliers as well as the labels associated to non outliers
            score = accuracy_score(labels[~non_outliers_mask], new_labels[~non_outliers_mask])

        res.append([i, score,clusters, outliers])
    #creating a dataframe with required info based on different eps values
    df = pd.DataFrame(res, columns=['eps', 'Score', 'Clusters', 'Outliers'], dtype=float)
    return df


def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()

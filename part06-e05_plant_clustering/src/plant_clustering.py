#!/usr/bin/env python3

import scipy
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    #creating a model for clustering given 3 centers
    model = KMeans(3, random_state = 0) # random_state = 0 makes it deterministic
    #loading dataset
    iris = load_iris()
    print(iris)
    print(iris.data)
    model.fit(iris.data)
    permutation = find_permutation(3, iris.target, model.labels_)
    #iris.target -> assigned label 1D array
    #creating labels based on what the model infered
    nl = [permutation[label] for label in model.labels_]
    score = accuracy_score(iris.target, nl)
    return score

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()

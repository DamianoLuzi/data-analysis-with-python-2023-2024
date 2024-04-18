#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree
import sklearn
import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    n = len(a)
    #creating the matrix 
    #-> n rows == number of words
    #-> len(alohabet) == number of letters in the alphabet
    feature_matrix = np.zeros((n, len(alphabet)))
    #there are as many features as letters in alphabet
    #associating every feature with tha number of times a letter appeared in the word

    #looping through words in a
    for i, word in enumerate(a):
        #looping through chars in each word
        for j, char in enumerate(alphabet):
            #counts how many times a char appears in the word
            count = word.count(char)  
            feature_matrix[i, j] = count
    
    return feature_matrix

def contains_valid_chars(s):
    for char in s:
        if char not in alphabet:
            return False
    return True

def get_features_and_labels():
    finnish = load_finnish()
    #converting every word to lowercase
    fl = [word.lower() for word in finnish]
    #filtering only words that contain valid chars
    f = [word for word in fl if contains_valid_chars(word)]
    english = list(load_english())
    el= [i.lower() for i in english if i[0].islower()]
    e = [i for i in el if contains_valid_chars(i)]
    
    #retrieving features
    finnish_feat = get_features(f)
    #target -> y -> 1D array containing the assigned labels
    finnish_targ = np.zeros((len(f), 1))
    #retrieving features
    english_feat = get_features(e)
    #target -> y -> 1D array containing the assigned labels
    english_targ = np.ones((len(e), 1))
    targ = np.concatenate((finnish_targ, english_targ))
    feat = np.concatenate((finnish_feat, english_feat))

    return feat, targ


def word_classification():
    feature_matrix, labels = get_features_and_labels()
    model = MultinomialNB() #because features are counts
    
    #splitting data into n_splits folds
    #one fold is used as validation , while the rest is trasining data
    cv_behaviour = sklearn.model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    score = cross_val_score(model, feature_matrix, np.ravel(labels), cv=cv_behaviour)
    return score


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()

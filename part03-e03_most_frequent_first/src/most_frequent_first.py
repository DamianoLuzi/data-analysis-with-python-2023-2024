#!C:\Python311\python.exe

import numpy as np

def most_frequent_first(a, c):
    # getting unique values from sorting the specified column
    u = np.unique(a[:,c], axis = 0, return_counts=True)
    print(u)
    #u is a tuble containg 2 arrays:
    #one contains found values, with no repetitions
    #one contains the number of occurrences for each value
    uniq_values,uniq_count = u
    #sorting the indices of uniq_count in descending order -> which effectively sorts the unique values based on their counts in descending order.
    count_sorted_ind = np.argsort(-uniq_count)
    # getting sorting column values sorted by their numb of occurencies
    #reshapes the resulting array into a 2D array with one row and as many columns as there are unique values.
    val_sorted_by_count = uniq_values[count_sorted_ind].reshape((1,-1))
    # getting array of indexes of that sorted array
    indxs = np.concatenate([np.where((a[:,c] == x))[0] for x in np.nditer(val_sorted_by_count)])
    return a[indxs]

def main():
    a = np.array([[5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
     [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
     [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
     [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
     [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
     [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
     [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
     [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
     [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
     [5, 9, 3, 0, 5, 0, 1, 2, 4, 2]])
    most_frequent_first(a,-1 )
    pass

if __name__ == "__main__":
    main()

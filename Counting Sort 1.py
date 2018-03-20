#!/bin/python3

import sys

def countingSort(arr):
    counts = {}
    for num in arr:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    
    #output counts in array starting from 0 to 99
    counts_arr = []
    for i in range(100):
        if i in arr:
            counts_arr.append(counts[i])
        else:
            counts_arr.append(0)
    
    print(' '.join(map(str, counts_arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))



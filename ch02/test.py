__author__ = 'cwang'
from collections import defaultdict
from collections import Counter
from pandas import DataFrame, Series
import numpy as np
import pandas as pd

def get_counts1(arr):
    counts = {}
    for item in arr:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def get_counts2(arr):
    counts = defaultdict(int)
    for item in arr:
        counts[item] += 1
    return counts

def top_counts(dict, n=10):
    value_pairs = [(count, tz) for tz, count in dict.items()]
    value_pairs.sort()
    return value_pairs[-n:]

if __name__ == '__main__':
    arr = ['cool', 'not', 'none', 'not', 'not', 'cool', 'none', 'none', 'none']
    # count1 = get_counts1(arr)
    count = get_counts2(arr)
    top = top_counts(count, n=2)
    count1 = Counter(arr)
    # print(count1.most_common(1))
    ls = np.array([1, 2, 2, 4, 2, 2])
    print(ls.argsort())
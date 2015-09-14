__author__ = 'cwang'
from collections import defaultdict
from collections import Counter
from pandas import DataFrame, Series
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

def get_names():
    pieces = []
    years = range(1880, 2011)
    for year in years:
        path = 'names/yob%d.txt' % year
        DF = pd.read_csv(path, names=['name', 'sex', 'births'])
        DF['year'] = year
        pieces.append(DF)
    names = pd.concat(pieces, ignore_index=True)
    return names

def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]

def get_quantile_count(group, q=0.5):
    group = group.sort_index(by='prop', ascending=False)
    mednum = group.prop.cumsum().searchsorted(q) + 1
    return mednum

if __name__ == '__main__':
    # arr = ['cool', 'not', 'none', 'not', 'not', 'cool', 'none', 'none', 'none']
    # # count1 = get_counts1(arr)
    # count = get_counts2(arr)
    # top = top_counts(count, n=2)
    # count1 = Counter(arr)
    # # print(count1.most_common(1))
    # ls = np.array([1, 2, 2, 4, 2, 2])
    # print(ls.argsort())
    #
    # dict = {}
    # dict['a'] = 1
    # dict['b'] = dict.pop('a')
    # names = get_names()
    # get_last_letter = lambda x: x[-1]
    # last_letters = names.name.map(get_last_letter)
    # last_letters.name = 'last_letter'
    # tbl = names.pivot_table(index=last_letters, columns=['sex', 'year'], values='births', aggfunc=sum)
    # letter_prop = tbl / tbl.sum().astype(float)
    # dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
    # dny_ts.plot()
    df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])

    df2.plot(kind='bar')
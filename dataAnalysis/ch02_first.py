# coding=UTF-8
__author__ = 'krilo'

### ch02 example
import json

path = 'data/usagov_bitly_data2012-03-16-1331923249.txt'
# json 的使用，列表推導式的表達法
records = [json.loads(line) for line in open(path)]
print records[0]
print records[0].get('tz')

# 下面的寫法是因為有的raw 中的 'tz'是空的
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print time_zones[:10]

# 得到前10的時區及總計
from collections import defaultdict


def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


print '前10個時區及統計：'
for top10 in top_counts(get_counts(time_zones)):
    print top10

print '使用 Pandas'

from pandas import DataFrame, Series
import pandas as pd;
import numpy as np

frame = DataFrame(records)
print frame['tz'][:10]


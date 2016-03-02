# coding=UTF-8
__author__ = 'krilo'

### ch02 example
import json

path = 'data/usagov_bitly_data2012-03-16-1331923249.txt'
"""
資料格式：
{ "a": "Mozilla\/5.0 (Windows NT 6.1; WOW64) AppleWebKit\/535.11 (KHTML, like Gecko) Chrome\/17.0.963.78 Safari\/535.11",
"c": "US", "nk": 1, "tz": "America\/New_York", "gr": "MA", "g": "A6qOVH", "h": "wfLQtf", "l": "orofrog",
"al": "en-US,en;q=0.8", "hh": "1.usa.gov", "r": "http:\/\/www.facebook.com\/l\/7AQEFzjSi\/1.usa.gov\/wfLQtf",
"u": "http:\/\/www.ncbi.nlm.nih.gov\/pubmed\/22415991", "t": 1331923247, "hc": 1331822918, "cy": "Danvers", "ll": [ 42.576698, -70.954903 ] }

"""

# json 的使用，列表推導式的表達法
records = [json.loads(line) for line in open(path)]
print "取得第一筆資料： ", records[0]
print "其中'tz'的值： ", records[0].get('tz')

# 下面的寫法是因為有的raw 中的 'tz'是空的
# records 為一dict , rec['tz'] 為 dict 生成式的運算式
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print "前10筆的時區：", time_zones[:10]

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

print "================================"
print '使用 Pandas\n'

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

frame = DataFrame(records)
# print type(frame)
print "summary view: \n 前10筆: \n", frame['tz'][:10]

tz_counts = frame['tz'].value_counts()
print "\nvalue_counts: 統計相同的城市(依數字排序):\n", tz_counts[:5]

clean_tz = frame['tz'].fillna('Missing')  # fillna 可以替換缺失值
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()

print "\n將NA補上： \n", tz_counts[:5]
print "\n其中Missing的有：", tz_counts['Missing'], "筆."

# 繪出圖形
ax = tz_counts[:10].plot(kind='barh', rot=0)
fig = ax.get_figure()
fig.savefig('asdf.png')

"""
    對 windows 與非windows用戶分開統計
"""
# 移除有缺失的 agent
cframe = frame[frame.a.notnull()]
operatingSystem = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
# print operatingSystem[:5]

# 根據時區對OS分組
by_tz_os = cframe.groupby(['tz', operatingSystem])
agg_count = by_tz_os.size().unstack().fillna(0)
print agg_count[:10]

# 根據最常出現排序
indexer = agg_count.sum(1).argsort()
print "最常出現時區： \n", indexer[:10]

# 印出堆疊圖
count_subset = agg_count.take(indexer)[-10:]
# print count_subset
ax2 = count_subset.plot(kind='barh', stacked=True)
ax2.get_figure().savefig('asdf2.png')
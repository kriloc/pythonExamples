# coding=UTF-8
__author__ = 'krilo'

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# GroupBy 技術
df = DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': np.random.randn(5),
    'data2': [1, 2, 3, 4, 5]
    # 'data2': np.random.randn(5)
})

print "df: \n", df

grouped = df['data1'].groupby([df['key1'], df['key2']])
print "採用 key1 + key2 分組：\n", grouped.mean()
# print "第二次分組：\n", grouped.mean().unstack()
print "採用列名作分組鍵：\n", df.groupby(['key1', 'key2']).size()  # size , 返回一個含有分組大小的 Series

print "對分組進行迭代：\n"
for name, group in df.groupby('key1'):
    print name
    print group



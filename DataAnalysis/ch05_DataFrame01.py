# coding=UTF-8
__author__ = 'krilo'

### ch05 example
from pandas import Series, DataFrame
import pandas as pd

data01 = {
    'state': ['ohio', 'ohio', 'ohio', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}
frame01 = DataFrame(data01)
print "DataFrmae 會自動加上索引 \n", frame01

frame01 = DataFrame(data01, columns=['year', 'state', 'pop'])
print "DataFrmae 指定列序列, 找不到的數據會產生NA值. \n", frame01

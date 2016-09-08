# coding:utf-8
import pandas as pd
from pandas import DataFrame, Series

df = DataFrame(['a', 'a', 'b', 'b', 'c', 'a'], columns=['name'])
name_dummy = pd.get_dummies(df.name)
print name_dummy

name_dummy.columns = ['u_a', 'u_b', 'u_c']
print name_dummy

df = df.join(name_dummy)
print df


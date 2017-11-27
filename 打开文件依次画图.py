import numpy as np
import pandas as pd
import datetime

'''此次步骤操作，只是为了改变在画时间序列时的图横坐标默认精确到秒上，我们将坐标字符串化，使横坐标精确到天就行'''
a = pd.date_range('2015/1/1','2015/5/1')
b = []
for i in a:
    i = datetime.datetime.strftime(i,'%Y-%m-%d')
    b.append(i)
c = pd.Series(b)
print(c)
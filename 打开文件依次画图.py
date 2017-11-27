import numpy as np
import pandas as pd
import datetime

'''等一下用numpy到来导出字符串的日期'''
a = pd.date_range('2015/1/1','2015/5/1')
b = []
for i in a:
    i = datetime.datetime.strftime(i,'%Y-%m-%d')
    b.append(i)
print(b)

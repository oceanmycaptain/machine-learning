import numpy as np
import pandas as pd



tmp = np.loadtxt('C:/Users/a/Desktop/关于自行车出行问题/第二次的数据/train.csv',dtype=np.str,delimiter=',')
data = tmp[1:,1:].astype(np.float)
for m in range(1, 9):
    data1 = np.zeros([49476,7])
    a = 0
    i = 0
    while a < len(data):
        if data[a][1] == m :
            data1[i] = data[a]
            a += 1
            i += 1

        else:
            a += 1

    data2 = pd.DataFrame(data1,columns=['week','month','day','mor or atf','take or park','station','number'])
    data2.to_csv('C:/Users/a/Desktop/关于自行车出行问题/第二次的数据/%d月份.csv'%m)


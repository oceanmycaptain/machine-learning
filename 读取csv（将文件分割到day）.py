import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt


tmp = np.loadtxt('C:/Users/a/Desktop/关于自行车出行问题/第二次的数据/train.csv',dtype=np.str,delimiter=',')
data = tmp[1:,1:].astype(np.float)


data2 = []
for a in range(1,2):
     for i in range(1,32):
        data1 = np.zeros([1596,7])
        n = 0
        m = 0
        while n < len(data):
            if data[n][1] == a and data[n][2] == i:
                data1[m] = data[n]
                m += 1
                n += 1
            else:
                n += 1
        #data2 = pd.DataFrame(data1,columns=['week','month','day','mor or atf','take or park','station','number'])
        #data2.to_csv('C:/Users/a/Desktop/总体数据/%s月的%s号.csv'%(a,i))
        add_num = data1.sum(axis=0)[6]
        if add_num != 0:
            data2.append(add_num)

data_time =pd.Series(data2,index = pd.date_range('1/1/2015',periods =len(data2)))
data_time.plot(kind = 'bar')
plt.show()



# data_time.to_csv('E:/关于自行车出行问题/第二次的数据/1234.csv')








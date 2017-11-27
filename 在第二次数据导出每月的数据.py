import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt

tmp = np.loadtxt('C:/Users/a/Desktop/关于自行车出行问题/第二次的数据/train.csv',dtype=np.str,delimiter=',')
data = tmp[1:,1:].astype(np.float)

a = 1
while a < 9:
#for a in range(1,9):用来画所有月份的图
    data2 = []
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
        add_num = data1.sum(axis=0)[6]
        if add_num != 0:
            data2.append(add_num)

    data_time =pd.Series(data2,index = pd.date_range('%d/1/2015'%a,periods =len(data2)))
    plt.ylim(0,30000)
    data_time.plot()#线状图
    #plt.show()
    fig = plt.gcf()#没有这一步，保存的图片会成为空白
    fig.savefig('C:/Users/a/Desktop/图片一/%d月数据.png'%a,pdi=1000,bbox_inches='tight')
    plt.close()
    plt.ylim(0,30000)
    data_time.plot(kind = 'bar')#柱状图
    fig = plt.gcf()
    fig.savefig('C:/Users/a/Desktop/图片一/%d月数据柱状图.png'%a,pdi=1000,bbox_inches='tight')
    plt.close()
    a += 1
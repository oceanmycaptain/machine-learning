import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

station_data = pd.read_csv('C:/Users/a/Desktop/Newstation_date.csv',index_col='date')
#用pd.read_csv时是不能用中文字符，不然会报错
#print(station_data['SHEDID1'])
for i in range(1,400):
    df = pd.Series(station_data['SHEDID%d'%i])
    plt.ylim(0,250)
    df.plot(kind = 'bar')
    #plt.show()
    fig = plt.gcf()  # 没有这一步，保存的图片会成为空白
    fig.savefig('E:每个车位1/%d号车位数据.png' % i, pdi=1200, bbox_inches='tight')
    plt.close()

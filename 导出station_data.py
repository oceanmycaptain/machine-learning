import pandas as pd
import numpy as np
data = pd.DataFrame(pd.read_csv('C:/Users/a/Desktop/train.csv'))
#在此处不能要出现中文字符，不然会报错的。
#a = data.loc[data['station']==1,['month','day','number']].head()
#head（）一般默认显示前5行
data2 = np.zeros([243,399])

for s in range(1,400):
    n = 0
    for m in range(1,9):
        day = int(data.loc[data['month']==m].day.max())+1
        #该行因为我们的图表中找到的是每个月对应的天数所以只好出此下策的方法
        for d in range(1,day):
            data1 = data.loc[(data['station']==s)&(data['month']==m)&(data['day']==d)].number.sum()
            #该loc（）函数为pandas中的用于搜索我们想要的内容
            data2[n][s-1] = int(data1)
            n += 1
data2 = pd.DataFrame(data2,index=pd.date_range('2015/1/1','2015/8/31'),columns=range(1,400))
#保存我们想要的格式和我们对应的每一列和每一行的定位
data2.to_csv('C:/Users/a/Desktop/Newstation_data.csv')
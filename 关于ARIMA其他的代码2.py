from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import stats
import datetime
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

txt1 = open('C:/Users/a/Desktop/123.txt')

for line in txt1:
    data = eval(line)

data_1 = {}
for key in data:
    key1=datetime.datetime.strptime(key,'%Y/%m/%d')
    key2=datetime.datetime.strftime(key1,'%Y-%m-%d')
    data_1[key2] = data[key]


b = tuple(data.keys())


data = np.load('C:/Users/a/Desktop/chewei/6.npy')
df = data[1]
df = pd.Series(df)
df.index = pd.Index(sm.tsa.datetools.dates_from_str(b))
df = df.diff(1)
df.dropna(inplace=True)
# df.plot()
# plt.show()

#检查平稳时间序列的自相关图和偏相关图
fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(df,lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(df,lags=40,ax=ax2)
plt.show()

#模型选择
#arma_mod20 = sm.tsa.ARMA(df,(2,0)).fit()
#print(arma_mod00.aic,arma_mod00.bic,arma_mod00.hqic)
#arma_mod180 = sm.tsa.ARMA(df,(18,2)).fit()
#print(arma_mod00.aic,arma_mod00.bic,arma_mod00.hqic)


#接下来检验残差序列
#resid = arma_mod180.resid
#print(sm.stats.durbin_watson(arma_mod180.resid))#此时DW值为1.967698当DW值显著接近0或4，则存在相关性，而接近2时，则不存在（一阶）自相关性。

#检查是否符合正态分布
# print(stats.normaltest(resid))
# fig = plt.figure(figsize=(12,6))
# ax = fig.add_subplot(111)
# fig = qqplot(resid,line='q',ax =ax ,fit=True)
# plt.show()

#Ljung-Box检验也叫Q检验
# r,q,p = sm.tsa.acf(resid.squeeze(),qstat=True)
# a = np.c_[range(1,41),r[1:],q,p]
# table = pd.DataFrame(a,columns=['lag','AC','Q','Prob(>Q)'])
# print(table.set_index('lag'))#prob值均大于0.05，所以残差序列不存在自相关性

#模型预测
# predict_sunspots = arma_mod180.predict('2015-07-31','2015-8-31',dynamic=True)
# print(predict_sunspots)
# fig,ax = plt.subplots(figsize = (12,6))
# ax = df.ix['2015-05-1':].plot(ax=ax)
# fig = arma_mod180.plot_predict('2015-07-31','2015-8-31',dynamic=True,ax=ax,plot_insample=False)
# plt.show()
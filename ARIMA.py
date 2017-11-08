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


a = tuple(data_1.values())

#print(data.keys())
df = np.array(a,dtype=np.float)
#print(a)
df = pd.Series(df)

# b = []
# for i in range(0,92):
#     b.append(i)
df.index = pd.Index(sm.tsa.datetools.dates_from_str(data.keys()))
#df.index = pd.Index(sm.tsa.datetools.dates_from_range('2000','2091'))
# df.index = pd.Index(b)
df = df.diff(1)#我们已经知道要使用一阶差分时间序列，因为对比发现1,2阶差不多。此时我们需要选择合适的p，q。
df.dropna(inplace=True)
# df.plot()
# plt.show()

#检查平稳时间序列的自相关图和偏自相关图
# fig = plt.figure(figsize=(12,6))
# ax1 = fig.add_subplot(211)
# fig = sm.graphics.tsa.plot_acf(df,lags=40,ax=ax1)
# ax2 = fig.add_subplot(212)
# fig = sm.graphics.tsa.plot_pacf(df,lags=40,ax=ax2)
# plt.show()

#模型选择
# arma_mod150 = sm.tsa.ARMA(df[1:],(15,0)).fit(disp=False)
# arma_mod00 = sm.tsa.ARMA(df[1:],(0,0)).fit(disp=False)
# arma_mod10 = sm.tsa.ARMA(df[1:],(1,0)).fit(disp=False)
#arma_mod01 = sm.tsa.ARMA(df[1:],(0,1)).fit(disp=False)
arma_mod50 = sm.tsa.ARMA(df,(5,0)).fit(disp=False)
# print(arma_mod150.aic,arma_mod150.bic,arma_mod150.hqic)
# print(arma_mod00.aic,arma_mod00.bic,arma_mod00.hqic)
# print(arma_mod10.aic,arma_mod10.bic,arma_mod10.hqic)#经过结果对比第一个（1,0）模型更加符合,但是选择后预测的效果是最糟糕的
# print(arma_mod01.aic,arma_mod01.bic,arma_mod01.hqic)
#print(arma_mod50.aic,arma_mod50.bic,arma_mod50.hqic)#而此模型更有预测的价值。

#接下来检验残差序列
resid = arma_mod50.resid
# print(sm.stats.durbin_watson(arma_mod50.resid))#此时DW值为1.967698当DW值显著接近0或4，则存在相关性，而接近2时，则不存在（一阶）自相关性。
# fig = plt.figure(figsize=(12,6))
# ax1 = fig.add_subplot(211)
# fig = sm.graphics.tsa.plot_acf(resid.squeeze(),lags=40,ax=ax1)
# ax2 = fig.add_subplot(212)
# fig = sm.graphics.tsa.plot_pacf(resid,lags=40,ax=ax2)
# print(sm.stats.durbin_watson(arma_mod11.resid))#所以残差序列不存在自相关性

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
predict_sunspots = arma_mod50.predict('2015-07-31','2015-8-31',dynamic=True)
print(predict_sunspots)
fig,ax = plt.subplots(figsize = (12,6))
ax = df.ix['2015-05-1':].plot(ax=ax)
fig = arma_mod50.plot_predict('2015-07-31','2015-8-31',dynamic=True,ax=ax,plot_insample=False)
plt.show()
#此次预测的模型居然最后成为了一条直线，奇怪这得好好看看选择自己的模型的问题
#经过选择其他的模型发现有些误差上分析不好的，但在预测上有一定的成效。
#关于此不科学的结果，我认为是我的原始数据就存在着所谓的白噪声，没有到达能进行该模型的前提。


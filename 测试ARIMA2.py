from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

dta=[10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186,6422,
6337,11649,11652,10310,12043,7937,6476,9662,9570,9981,9331,9449,6773,6304,9355,
10477,10148,10395,11261,8713,7299,10424,10795,11069,11602,11427,9095,7707,10767,
12136,12812,12006,12528,10329,7818,11719,11683,12603,11495,13670,11337,10232,
13261,13230,15535,16837,19598,14823,11622,19391,18177,19994,14723,15694,13248,
9543,12872,13101,15053,12619,13749,10228,9725,14729,12518,14564,15085,14722,
11999,9390,13481,14795,15845,15271,14686,11054,10395]
dta = np.array(dta,dtype=np.float)
#print(dta)
dta = pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2090'))
#print(dta.index)
#dta.plot(figsize=(12,6))
#plt.show()


# arma_mod80 = sm.tsa.ARMA(dta,(8,0)).fit()
# print(arma_mod80.aic,arma_mod80.bic,arma_mod80.hqic)

#检查平稳时间序列的自相关图和偏自相关图
fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta,lags=40,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta,lags=40,ax=ax2)
plt.show()

#resid = arma_mod80.resid
##print(stats.normaltest(resid))
# fig = plt.figure(figsize=(12,6))
# ax = fig.add_subplot(111)
# fig = qqplot(resid,line='q',ax=ax,fit=True)
##plt.show()

# predict_dta = arma_mod80.predict('2090','2120',dynamic=True)
# #print(predict_dta)
# fig,ax = plt.subplots(figsize = (12,6))
# ax = dta.ix['2000':].plot(ax=ax)
# predict_dta.plot(ax=ax)
# plt.show()
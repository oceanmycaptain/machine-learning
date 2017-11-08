from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import stats
import datetime
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
dta = pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2000','2089'))
dta = dta.diff(1)
dta.dropna(inplace=True)
#diff1.plot(figsize = (12,6))
#plt.show()

#自相关量和偏相关量
# fig = plt.figure(figsize=(12,6))
# ax1 = fig.add_subplot(211)
# fig = sm.graphics.tsa.plot_acf(dta,lags=40,ax=ax1)
# ax2 = fig.add_subplot(212)
# fig = sm.graphics.tsa.plot_pacf(dta,lags=40,ax=ax2)
# plt.show()

# arma_mod00 = sm.tsa.ARMA(dta,(0,0)).fit(disp=False)
arma_mod70 = sm.tsa.ARMA(dta,(7,0)).fit(disp=False)
# arma_mod60 = sm.tsa.ARMA(dta,(6,0)).fit(disp=False)
#arma_mod140 = sm.tsa.ARMA(dta,(14,0)).fit(disp=False)
# print(arma_mod00.aic,arma_mod00.bic,arma_mod00.hqic)
# print(arma_mod70.aic,arma_mod70.bic,arma_mod70.hqic)
# print(arma_mod60.aic,arma_mod60.bic,arma_mod60.hqic)
# print(arma_mod140.aic,arma_mod140.bic,arma_mod140.hqic)

resid = arma_mod70.resid
#print(sm.stats.durbin_watson(resid))
# fig = plt.figure(figsize=(12,6))
# ax = fig.add_subplot(111)
# fig = qqplot(resid,line='q',ax =ax ,fit=True)
# plt.show()

predict_sunspots = arma_mod70.predict('2089','2100',dynamic=True)
print(predict_sunspots)
fig,ax = plt.subplots(figsize = (12,6))
ax = dta.ix['2000':].plot(ax=ax)
fig = arma_mod70.plot_predict('2089','2100',dynamic=True,ax=ax,plot_insample=False)
plt.show()

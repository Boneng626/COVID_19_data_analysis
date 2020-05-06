import pandas as pd
from pylab import *
import numpy as np
from scipy.optimize import curve_fit
from datetime import datetime


region= 'US'

df8 = pd.read_csv('covid_19_data.csv')
df8['ObservationDate']=pd.to_datetime(df8['ObservationDate'])
dfp = df8[['ObservationDate', 'Country/Region','Confirmed']]
dfp1 = dfp[['ObservationDate','Confirmed']].loc[dfp['Country/Region'] == region]
dfp2 = dfp1.groupby('ObservationDate',as_index= False).sum()

data=dfp2
print(data.head())
x= data['ObservationDate']
y=data['Confirmed']


#logistic模型预测
def logistic_increase_function(t, K, P0, r):
     r=0.13
     t0 = 1
     exp_value = np.exp(r * (t - t0))
     return (K * exp_value * P0) / (K + (exp_value - 1) * P0)


ts = data['ObservationDate']
t = pd.Series(np.arange(84),index=ts)
P = data['Confirmed'] # 最小二乘拟合
P = np.array(P)
popt, pocv = curve_fit(logistic_increase_function, t, P)
#所获取的opt皆为拟合系数

P_predict=logistic_increase_function(t,popt[0],popt[1],popt[2])
dates = pd.date_range(start='2020-4-15',periods=60)
d=dict(pd.Series(np.arange(84,144),index=dates))
print(d)
future = pd.Series(np.arange(84,144),index=dates)
future=np.array(future)
future_predict=logistic_increase_function(future,popt[0],popt[1],popt[2])

def predict(month,day):

 dt = datetime(2020, month, day, 00, 00) # datetime
 #print(dt)
 global people_sick
 people_sick=int(logistic_increase_function(d[pd.Timestamp(dt)],popt[0],popt[1],popt[2]))

 print(people_sick)

predict(5,30)


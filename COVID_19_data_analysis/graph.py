import pandas as pd
#from pylab import *
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#from datetime import datetime
import tkinter as tk

region= 'Mainland China'

df8 = pd.read_csv('covid_19_data.csv')
df8['ObservationDate']=pd.to_datetime(df8['ObservationDate'])
dfp = df8[['ObservationDate', 'Country/Region','Confirmed']]
dfp1 = dfp[['ObservationDate','Confirmed']].loc[dfp['Country/Region'] == region]
dfp2 = dfp1.groupby('ObservationDate',as_index= False).sum()

data=dfp2
'''print(data.head())
x= data['ObservationDate']
y=data['Confirmed']'''

'''plt.plot(x,y,color='green',marker='o',linestyle='solid',label='Confirmed')
plt.title('COVID-19 Trend '+ region)
plt.ylabel('Cases')
plt.xlabel("Date")
plt.show()'''

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
P_predict=logistic_increase_function(t,popt[0],popt[1],popt[2])
dates = pd.date_range(start='2020-4-15',periods=60)
d=dict(pd.Series(np.arange(84,144),index=dates))
print(d)
future = pd.Series(np.arange(84,144),index=dates)
future=np.array(future)
future_predict=logistic_increase_function(future,popt[0],popt[1],popt[2])

plt.plot(t,P,'s',label ='Fact')
plt.plot(t,P_predict,'r',label ='prediction model')
plt.title('COVID-19 '+ region)
plt.xlabel('Date')
plt.ylabel('Cases')
plt.legend(loc=0)
plt.show()

'''plot3=plt.plot(future,future_predict,'s',label='Predict')
plt.title('COVID-19 Prediction '+ region)
plt.xlabel('Date')
plt.ylabel('Cases')
plt.show()'''


'''df7['date_onset_symptoms']=pd.to_datetime(df7['date_onset_symptoms'],format='%d.%m.%y')
df7['date_admission_hospital']=pd.to_datetime(df7['date_admission_hospital'])
df7['date_confirmation']=pd.to_datetime(df7['date_confirmation'])
dfp = df7[['date_onset_symptoms', 'date_admission_hospital','date_confirmation']]
dfp1 = dfp[['ObservationDate','Confirmed']].loc[dfp['country'] == 'China']
#dfp2 = dfp1.groupby('ObservationDate',as_index= False).sum()
s1 = pd.Series(dfp['date_onset_symptoms'])
s2 = pd.Series(dfp['date_admission_hospital'])
print(s2-s1)'''

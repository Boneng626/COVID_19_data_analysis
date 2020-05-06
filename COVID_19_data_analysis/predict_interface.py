import tkinter as tk
import predict
import pandas as pd
from pylab import *
import numpy as np
from scipy.optimize import curve_fit
from datetime import datetime
#from pylab import *
from scipy.optimize import curve_fit
#from datetime import datetime


window = tk.Tk()
window.title('Future Predict')
window.geometry('500x300')

l1 = tk.Label(window, bg='green', fg='white', width=20, text='Select date')
l1.pack()
t1 = tk.Text(window,bg='yellow',height=4)
#t1.insert("end","The estimated cases number in US until ")
#t1.insert("end","1187645")
t1.pack()
tk.Label(window, text='Month:').place(x=100, y=230)
var_month = tk.IntVar()
var_month = int(var_month.get())

'''var_month = tk.StringVar()
var_month =var_month.get()'''

#datetime.strptime(var_month, '%m')
entry_month = tk.Entry(window, textvariable=var_month)
entry_month.place(x=150, y=230)


def print_selection(v):
    l1.config(text='you have selected ' + v)
    l1.config()
    v = int(s1.get())
    predict.predict(5,v)
    t1.insert('end', 'Estimated cases in US until ' + '5'+ '/' + str(v) + '/' + '2020 ')
    t1.insert('end', predict.people_sick)

s1 = tk.Scale(window, label='Select date', from_=1, to=30, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=3, command=print_selection)
s1.pack()
#day = s1.get()
#dt = datetime(2020, var_month, day, 00, 00)
#print(dt)
def logistic_increase_function(t, K, P0, r):

     #r=0.13
     t0 = 1
     exp_value = np.exp(r * (t - t0))
     return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

def value():
 global r
 global region
 if (var1.get() == 1) & (var2.get() == 0):
       r=0.29
       region = 'Mainland China'
 elif (var1.get() == 0) & (var2.get() == 1):
       r=0.13
       region = 'US'
 else :
       r=0.13
       region = 'US'

def trend():

  window1= tk.Toplevel()
  window1.title('The COVID-19 Trend')
  window1.geometry('600x600')


  df8 = pd.read_csv('covid_19_data.csv')
  df8['ObservationDate']=pd.to_datetime(df8['ObservationDate'])
  dfp = df8[['ObservationDate', 'Country/Region','Confirmed']]
  dfp1 = dfp[['ObservationDate','Confirmed']].loc[dfp['Country/Region'] == region]
  dfp2 = dfp1.groupby('ObservationDate',as_index= False).sum()
  data=dfp2

  def logistic_increase_function(t, K, P0, r):

     #r=0.13
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
     #d1={v: k for k, v in d.items()}
     #print(d1)
  #future = pd.Series(np.arange(84,144),index=dates)
  #future=np.array(future)
  #future_predict=logistic_increase_function(future,popt[0],popt[1],popt[2])
  plt.plot(t,P,'s',label ='Fact')
  plt.plot(t,P_predict,'r',label ='prediction model')
  plt.title('COVID-19 '+ region)
  plt.xlabel('Date')
  plt.ylabel('Cases')
  plt.legend(loc=0)
  plt.savefig('2.png')

  canvas = tk.Canvas(window1, width=800, height=600)
  global image_file1
  image_file1 = tk.PhotoImage(file = '2.png')
  canvas.create_image(0, 0, anchor='nw', image=image_file1)
  canvas.pack(side='left')



def Area():
 window2= tk.Toplevel()
 window2.title('The COVID-19 Area')
 window2.geometry('600x600')
 if (var1.get() == 1) & (var2.get() == 0):
   region='China'
 elif (var1.get() == 0) & (var2.get() == 1):
   region='United States'
 else:
   region='United States'

 df7 = pd.read_csv(r'COVID19_open_line_list.csv')
 df7.loc[df7['country']==region].plot.hexbin(x='latitude', y='longitude', gridsize=30)
 plt.xlabel('latitude')
 plt.ylabel('longitude')
 plt.title('Area Analysis '+ region )
 plt.savefig('3.png')

 canvas = tk.Canvas(window2, width=800, height=600)
 image_file3 = tk.PhotoImage(file = '3.png')
 canvas.create_image(0, 0, anchor='nw', image=image_file3)
 canvas.pack(side='left')
 window2.mainloop()

var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='China',variable=var1, onvalue=1, offvalue=0, command=value)
c1.pack()
c2 = tk.Checkbutton(window, text='US',variable=var2, onvalue=1, offvalue=0, command=value)
c2.pack()

b1 = tk.Button(window, text='Show Trend', font=('Arial', 12), width=10,height=1,command=trend)
b1.pack()
b2 = tk.Button(window, text='Show Area', font=('Arial', 12), width=10,height=1,command=Area)
b2.pack()

window.mainloop()

'''df8 = pd.read_csv('covid_19_data.csv')
df8['ObservationDate']=pd.to_datetime(df8['ObservationDate'])
dfp = df8[['ObservationDate', 'Country/Region','Confirmed']]
dfp1 = dfp[['ObservationDate','Confirmed']].loc[dfp['Country/Region'] == "Mainland China"]
dfp2 = dfp1.groupby('ObservationDate',as_index= False).sum()
data=dfp2
print(data)'''

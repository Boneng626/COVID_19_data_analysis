import tkinter as tk
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import tkinter.messagebox
import os
import predict_interface

pd.set_option('display.max_columns', None)
window = tk.Tk()

window.title('COVID-19')
window.geometry('600x400')

tk.Label(window, text='Country/Region:', font=('Arial', 14)).place(x=10, y=175)
tk.Label(window, text='Month:', font=('Arial', 14)).place(x=10, y=215)
tk.Label(window, text='Day:', font=('Arial', 14)).place(x=10, y=255)
tk.Label(window, text='Year:', font=('Arial', 14)).place(x=10, y=295)

var_region = tk.StringVar()
var_region.set('Example: China')
entry_region = tk.Entry(window, textvariable=var_region, font=('Arial', 14))
entry_region.place(x=130,y=175)

var_month = tk.StringVar()
var_month.set('Example: 1,2...11,12')
entry_month = tk.Entry(window, textvariable=var_month, font=('Arial', 14))
entry_month.place(x=130,y=215)

var_day = tk.StringVar()
var_day.set('Example: 1,2...30,31')
entry_day = tk.Entry(window, textvariable=var_day, font=('Arial', 14))
entry_day.place(x=130,y=255)

var_year= tk.StringVar()
var_year.set('19 or 20')
entry_year= tk.Entry(window, textvariable=var_year, font=('Arial', 14))
entry_year.place(x=130,y=295)

df1 = pd.read_csv('time_series_covid_19_confirmed.csv')
df2 = pd.read_csv('time_series_covid_19_confirmed_US.csv')
df3 = pd.read_csv('time_series_covid_19_deaths.csv')
df4 = pd.read_csv('time_series_covid_19_deaths_US.csv')
df5 = pd.read_csv('time_series_covid_19_recovered.csv')
df6 = pd.read_csv('COVID19_line_list_data.csv')
df7 = pd.read_csv(r'COVID19_open_line_list.csv')
df8 = pd.read_csv('covid_19_data.csv')

t1 = tk.Text(window,bg='green',height=4)
t1.pack()
t2 = tk.Text(window,bg='green',height=4)
t2.pack()

def region():
 global month
 global day
 global year
 region = var_region.get()
 month  = var_month.get()
 day = var_day.get()
 year = var_year.get()
 a = list(df1['Country/Region'].unique())
 b = list(df3['Country/Region'].unique())
 c=  list(df5['Country/Region'].unique())
 if region in a and region in b and region in c:
        dict1 = dict(df1.loc[df1['Country/Region'] == region].iloc[:, 4:].apply(sum))
        print('Cases confirmed until ' + month + '/' + day + '/' + year+' ')
        print(dict1[month + '/' + day + '/' + year])
        t1.insert('end', 'Cases confirmed until ' + month + '/' + day + '/' + year+' ')
        t1.insert('end', dict1[month + '/' + day + '/' + year])

        dfa = df1.iloc[:, 4:].T.shift(-1) - df1.iloc[:, 4:].T
        result1 = pd.concat([df1['Country/Region'], dfa.T], axis=1)
        dict_a = dict(result1.loc[df1['Country/Region'] == region].iloc[:, 4:].apply(sum))
        print('Daily cases confirmed  ')
        print(dict_a[month + '/' + day + '/' + year])
        t2.insert('end', 'Daily cases confirmed ')
        t2.insert('end', dict_a[month + '/' + day + '/' + year])

        dict2 = dict(df3.loc[df3['Country/Region'] == region].iloc[:, 4:].apply(sum))
        print('Deaths until ' + month + '/' + day + '/' + year+' ')
        print(dict2[month + '/' + day + '/' + year])
        t1.insert('end', 'Deaths until ' + month + '/' + day + '/' + year+' ')
        t1.insert('end', dict2[month + '/' + day + '/' + year])

        dfb = df3.iloc[:, 4:].T.shift(-1) - df3.iloc[:, 4:].T
        result2 = pd.concat([df3['Country/Region'], dfb.T], axis=1)
        dict_b = dict(result2.loc[df3['Country/Region'] == region].iloc[:, 4:].apply(sum))
        print('Daily deaths  ')
        print(dict_b[month + '/' + day + '/' + year])
        t2.insert('end', 'Daily deaths ')
        t2.insert('end', dict_b[month + '/' + day + '/' + year])

        dict3 = dict(df5.loc[df5['Country/Region'] == region].iloc[:, 4:].apply(sum))
        print('Recovered until ' + month + '/' + day + '/' + year+' ')
        print(dict3[month + '/' + day + '/' + year])
        t1.insert('end', 'Recovered until ' + month + '/' + day + '/' + year+' ')
        t1.insert('end', dict3[month + '/' + day + '/' + year])

        dfc = df5.iloc[:, 4:].T.shift(-1) - df5.iloc[:, 4:].T
        result3 = pd.concat([df5['Country/Region'], dfc.T], axis=1)
        dict_c = dict(result3.loc[df5['Country/Region'] == region].iloc[:, 4:].apply(sum))
        print('Daily recovered  ')
        print(dict_c[month + '/' + day + '/' + year])
        t2.insert('end', 'Daily recovered ')
        t2.insert('end', dict_c[month + '/' + day + '/' + year])

btn_1 = tk.Button(window, text='Search data',command=region)
btn_1.place(x=120, y=340)

def symptom():

 window_result= tk.Toplevel()
 window_result.title('Most common symptoms until')
 window_result.geometry('400x200')
 try:
  word_string1=' '.join(str(v) for v in df7['symptoms'])
  wordcloud1 = WordCloud(stopwords={'nan'},
                          background_color='white',
                      max_words=100,
                        collocations=False).generate(word_string1)
  wordcloud1.to_file('1.gif')

  canvas = tk.Canvas(window_result, width=400, height=200)
  global image_file
  image_file = tk.PhotoImage(file = '1.gif')
  canvas.create_image(0, 0, anchor='nw', image=image_file)
  canvas.pack(side='top')
 except:
   tk.messagebox.showerror(message='No enough data')




btn_2 = tk.Button(window, text='Search symptoms',command=symptom)
btn_2.place(x=220, y=340)

'''def predict():
 os.system('predict_interface.py')

btn_3 = tk.Button(window, text='predict',command=predict())
btn_3.place(x=350, y=340)'''

def transfer():
    os.system('predict_interface.py')
btn_3 = tk.Button(window, text='Next',command=transfer)
btn_3.place(x=350, y=340)

window.mainloop()

'''
df = df7[['date_confirmation','symptoms']]
print(df)

print(np.where(df7['date_confirmation']=='04.02.2020'))
'''


'''df8['ObservationDate']=pd.to_datetime(df8['ObservationDate'])
dfp = df8[['ObservationDate', 'Country/Region','Confirmed']]
dfp1 = dfp[['ObservationDate','Confirmed']].loc[dfp['Country/Region']=='Mainland China']
dfp2 = dfp1.groupby('ObservationDate',as_index= False).sum()

print(dfp2)
'''

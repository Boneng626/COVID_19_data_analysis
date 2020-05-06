import tkinter as tk
import tkinter.messagebox
import pymysql
import mysql

connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='626626626',
                             db='User')

cursor = connection.cursor()
sql = "SELECT user_name FROM Users "
cursor.execute(sql)
alldata = list(cursor.fetchall())
window_user= tk.Tk()
window_user.title('Administrator')
window_user.geometry('500x300')
var1 = tk.StringVar()
l = tk.Label(window_user, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
l.pack()
# 创建一个方法用于按钮的点击事件
def print_selection():
    value = lb1.get(lb1.curselection())
    var1.set(value)
b1 = tk.Button(window_user, text='Select an user to continue', width=25, height=2, command=print_selection)
b1.pack()
lb1 = tk.Listbox(window_user)

for item in alldata:
    lb1.insert('end', item)
lb1.pack()


def do():
    pass

menubar = tk.Menu(window_user)

usermenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Users Options', menu=usermenu)

usermenu.add_command(label='Delete this user', command=mysql.deleteData(var1))
usermenu.add_command(label='Reset Password', command=mysql.resetPasswprd(var1))
usermenu.add_separator()
usermenu.add_command(label='Exit', command=window_user.quit)

querymenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Queries Options', menu=querymenu)
querymenu.add_command(label='Add this Query', command=do)
querymenu.add_command(label='Delete this Query', command=do)


# menubar
window_user.config(menu=menubar)

window_user.mainloop()

import tkinter as tk
import tkinter.messagebox
import pymysql
import mysql
import os

connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='626626626',
                             db='User')


cursor = connection.cursor()


window = tk.Tk()
window.title('COVID-19 Application')
window.geometry('800x450')

canvas=tk.Canvas(window,height=450,width=800)
imagefile=tk.PhotoImage(file='/Users/liangboneng/Desktop/p2.png')
image=canvas.create_image(0,0,anchor='center',image=imagefile)
canvas.pack(side='top')

tk.Label(window, text='User:').place(x=250, y=150)
tk.Label(window, text='Password:').place(x=250, y=190)
# 用户名输入框
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=350, y=150)
# 密码输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=350, y=190)


def usr_log_in():
    global name
    global password
    global usr_name
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    if usr_name == 'admin' and usr_pwd == 'admin':
        os.system('Python administrator.py')

    elif usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='Empty username or password')

    sql = "SELECT * FROM Users \
       WHERE user_name = '%s'" % (usr_name)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        try:
            name = row[1]
            password = row[2]
        except:
            name = None
            password = None
        else:
            if usr_pwd == password:
                tk.messagebox.showinfo(title='welcome',
                                       message='Hello：' + usr_name)
                os.system('Python data_analysis.py')
            elif usr_pwd != password:
                tk.messagebox.showerror(message='Invalid Password')
            if usr_name != name:
                is_signup = tk.messagebox.askyesno('Welcome', 'Not existing user, register now?')

                if is_signup:
                    usr_sign_up()


# 注册函数

def usr_sign_up():
    # 确认注册时的相应函数

    def signtowcg():
        global name
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        if np == '' or nn == '':
            tk.messagebox.showerror('Error', 'Empty user name or password')
        elif np != npf:
            tk.messagebox.showerror('Error', 'password not match')
        # 检查用户名存在、密码为空、密码前后不一致
        sql = "SELECT * FROM Users \
        WHERE user_name = '%s'" % (nn)
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            try:
                name = row[1]
            except:
                name = None
            else:
                if nn == name:
                    tk.messagebox.showerror('Error', 'User already exists')

                # 注册信息没有问题则将用户名密码写入数据库
                else:
                    mysql.insertData(3, nn, np)
                    tk.messagebox.showinfo('Welcome', 'Successfully sign up!')
                    # 注册成功关闭注册框
                    window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up')

    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='User：').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Enter password：').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Enter password again ：').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)

    bt_confirm_sign_up = tk.Button(window_sign_up, text='Sign up',
                                   command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)


def usr_sign_quit():
    window.destroy()



bt_login = tk.Button(window, text='Log in', command=usr_log_in)
bt_login.place(x=250, y=230)
bt_logup = tk.Button(window, text='Sign up', command=usr_sign_up)
bt_logup.place(x=400, y=230)
bt_logquit = tk.Button(window, text='Exit', command=usr_sign_quit)
bt_logquit.place(x=505, y=230)

window.mainloop()

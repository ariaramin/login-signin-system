
from tkinter import messagebox
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Notebook
import time
from database import *

master = Tk()
note = Notebook()

Sign_in = Frame()
Log_in = Frame()

note.add(Sign_in, text = 'SignIn')
note.add(Log_in, text = 'LogIn')
note.grid(row = 0, column = 0)

#Username validation
def user_valid(a,b,c):
    if account(s_user.get()).get() != ():
        user.config(bg='red')
    elif len(s_user.get()) < 3:
        user.config(bg='red')
    else:
        user.config(bg='green')

#Username validation for login page
def loguser_valid(a,b,c):
    if account(sl_user.get()).get() != ():
        loguser.config(bg='green')
    else:
        loguser.config(bg='red')

#Email validation
def email_valid(a,b,c):
        if '@gmail.com' in s_email.get() and len(s_email.get()) >15 :
            email.config(bg="green")

        elif '@yahoo.com' in s_email.get() and len(s_email.get()) >15 :
            email.config(bg="green")
            
        else:
            email.config(bg='red')

#SignIn
def send_data():
    if s_user.get() and s_email.get() and s_password.get() != '':
        if account(s_user.get()).get() == ():
            signin(s_user.get().lower(),
                    s_email.get().lower(),
                    s_password.get().lower())

            s_user.set('')
            s_email.set('')
            s_password.set('')
    else:
        messagebox.showerror('Error', 'Filed all informations')

#Login
def Login():
    user = sl_user.get()
    password = sl_password.get()
    info = login(user,password).get()
    if user and password != '':
        if account(user).get() == ():
            messagebox.showerror('Error', 'This username does not exict')
        else:
            for users in account(user).get():
                if users[3] != password:
                    messagebox.showwarning('Warning', 'Password is not corroct')
                else:
                    messagebox.showinfo('Wellcome', 'Hello {}'.format(user))
                    
    else:
        messagebox.showerror('Error', 'Filed all informations')

#Forgot password
def forgot_pass():
    def email_validation(a,b,c):
        if '@gmail.com' in ef_email.get() and len(ef_email.get()) >15 :
            email_val.config(bg="green")

        elif '@yahoo.com' in ef_email.get() and len(ef_email.get()) >15 :
            email_val.config(bg="green")

        else:
            email_val.config(bg='red')

    def get_pass():
        email = ef_email.get()
        password = getpass(email).get()
        if password != ():
            for pas in password:
                forgotpass.set(pas[3])
        else:   
            forgotpass.set('This email does not exist! ')

    top = Toplevel()
    Label(top, text='Enter your email :', font=font).grid(row = 0, column = 0)
    ef_email = StringVar()
    ef_email.trace('w', email_validation)
    email_val = Entry(top, textvariable=ef_email, font=font)
    email_val.grid(row = 1, column = 0)
    forgotpass = StringVar()
    Label(top, textvariable=forgotpass, font=font).grid(row = 2, column = 0)
    Button(top, text='Get your password', font=font, command=get_pass).grid(row = 3, column = 0)

#SignIn page
font = Font(family='Verdana', size=13)

Label(Sign_in, text='Username :', font=font).grid(row = 0, column = 0)
s_user = StringVar()
s_user.trace('w', user_valid)
user = Entry(Sign_in, textvariable=s_user, font=font)
user.grid(row = 1, column = 0)

Label(Sign_in, text='Email :', font=font).grid(row = 2, column = 0)
s_email = StringVar()
s_email.trace('w', email_valid)
email = Entry(Sign_in, textvariable=s_email, font=font)
email.grid(row = 3, column = 0)

Label(Sign_in, text='Password :', font=font).grid(row = 4, column = 0)
s_password = StringVar()
Entry(Sign_in, textvariable=s_password, font=font).grid(row = 5, column = 0)

Button(Sign_in, text = 'SignIn',font=font, width=20, command=send_data).grid(row = 6, column = 0)

#LogIn page
Label(Log_in, text='Username :', font=font).grid(row = 0, column = 0)
sl_user = StringVar()
sl_user.trace('w', loguser_valid)
loguser = Entry(Log_in, textvariable=sl_user, font=font)
loguser.grid(row = 1, column = 0)

Label(Log_in, text='Password :', font=font).grid(row = 2, column = 0)
sl_password = StringVar()
Entry(Log_in, textvariable=sl_password, font=font).grid(row = 3, column = 0)

Button(Log_in, text = 'SignIn',font=font, width=20, command=Login).grid(row = 4, column = 0)
Button(Log_in, text = 'Forgot your password?!',font=font, width=20, command=forgot_pass).grid(row = 5, column = 0)

master.mainloop()
from tkinter import *

def getvals():
    print(f"the password is {uservalue.get()}")
    print(f"the password is {passvalue.get()}")


root = Tk()
root.geometry("650x250")    

user = Label(root, text="username")
password = Label(root, text="password")
user.grid()
password.grid(row=1)

# variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="submit", command=getvals).grid()

root.mainloop()
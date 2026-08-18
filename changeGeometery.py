from tkinter import *
def getvals():
    
    width = firstentry.get()
    height = secondentry.get()
    root.geometry(f"{width}x{height}")
    
root = Tk()


root.geometry("650x250")

value1 = Label(root, text="Enter width")
value2 = Label(root, text="Enter height")
value1.grid()
value2.grid(row=1)

firstentry = Entry(root)
secondentry = Entry(root)

firstentry.grid(row=0, column=1)
secondentry.grid(row=1, column=1)

Button(text="apply", command=getvals).grid()
root.mainloop()
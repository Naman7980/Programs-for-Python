from tkinter import *
root = Tk()

root.geometry("355x248")
root.title("aab banega na kaam ka samaan")

def myfun():
    print("i am a smart kid")

# mymenu = Menu(root)
# mymenu.add_command(label="file", command=myfun)    
# mymenu.add_command(label="exit", command=quit)
# root.config(menu=mymenu)

yourmenubar = Menu(root)
m1 = Menu(yourmenubar)
m1.add_command(label="new project", command=myfun)
m1.add_command(label="save", command=myfun)
m1.add_command(label="save as", command=myfun)
m1.add_command(label="print", command=myfun)
root.config(menu=yourmenubar)

yourmenubar.add_cascade(label="file", menu=m1)
    
root.mainloop()
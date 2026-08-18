from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Naman ki gui")

widget = Canvas(root, width=canvas_width, height=canvas_height)
widget.pack()

widget.create_oval(100,100,200,300)

root.mainloop()

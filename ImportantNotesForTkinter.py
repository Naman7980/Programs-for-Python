import tkinter as tk

root = tk.Tk()
root.title("Tkinter Frame Example")

# Create a frame with border and padding
frame1 = tk.Frame(root, bg="lightblue", borderwidth=5, relief="ridge")
frame1.pack(side="left", fill="both", expand=True, padx=10, pady=10)

frame2 = tk.Frame(root, bg="lightgreen", borderwidth=5, relief="groove")
frame2.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Add widgets inside frames
tk.Label(frame1, text="This is Frame 1", bg="lightblue").pack(pady=20)
tk.Button(frame1, text="Click Me").pack()

tk.Label(frame2, text="This is Frame 2", bg="lightgreen").pack(pady=20)
tk.Button(frame2, text="Another Button").pack()

root.mainloop()

#  Key Frame Options
# bg – Background color.
# borderwidth – Thickness of the border.
# relief – Border style (flat, raised, sunken, ridge, groove).
# padx, pady – Padding inside the frame.
# pack, grid, place – Layout managers to position frames

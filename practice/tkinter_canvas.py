from tkinter import *

window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()
canvas.create_oval(100, 50, 300, 250, fill="white")
canvas.create_oval(150, 100, 180, 130, outline="black")
canvas.create_oval(220, 100, 250, 130, outline="black")
canvas.create_arc(150, 150, 250, 225, outline="black", start=180, extent=180)
window.mainloop()
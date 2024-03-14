from tkinter import *

window = Tk()
canvas = Canvas(window, width=400, height=400)
canvas.pack()
canvas.create_oval(100, 100, 300, 300, fill="yellow")
canvas.create_oval(130, 150, 180, 200, fill="white")
canvas.create_oval(220, 150, 270, 200, fill="white")
canvas.create_oval(145, 165, 170, 190, fill="black")
canvas.create_oval(230, 165, 255, 190, fill="black")
canvas.create_arc(150, 200, 250, 275, start=180, extent=180, fill="red")
window.mainloop()
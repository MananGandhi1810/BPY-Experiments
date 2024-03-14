from tkinter import *
from tkinter import messagebox

def button_clicked():
    messagebox.showinfo("Hello!", message="Hello! I am Manan Gandhi")

window = Tk()
button = Button(window, text="Hello!", command=button_clicked)
button.place(relx=0.5, rely=0.5, anchor="center")
window.mainloop()
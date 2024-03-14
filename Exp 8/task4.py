from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("A simple GUI")
label = Label(window, text="This is our first GUI!")
label.pack()
def greet():
    messagebox.showinfo("Greeting", "Hello!")
button1 = Button(window, text="Greet", command=greet)
button1.pack()
button2 = Button(window, text="Close", command=window.quit)
button2.pack()
window.mainloop()
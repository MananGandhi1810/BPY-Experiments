from tkinter import Checkbutton, Tk, Label, Entry, Button

window = Tk()
window.title("Hello world")
cb1 = Checkbutton(window, text="Python")
cb1.pack()
cb2 = Checkbutton(window, text="Dart")
cb2.pack()
cb3 = Checkbutton(window, text="Javascript")
cb3.pack()
window.mainloop()

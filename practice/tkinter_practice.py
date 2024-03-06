from tkinter import *

window = Tk()
window.title("Hello!")
celsius_label = Label(window, text="Celsius")
celsius_label.grid(row=0, column=0)
celsius_entry = Entry(window)
celsius_entry.grid(row=0, column=1)
fahrenheit_label = Label(window, text="Fahrenheit")
fahrenheit_label.grid(row=1, column=0)
fahrenheit_entry = Entry(window)
fahrenheit_entry.grid(row=1, column=1)

def convert():
    celsius = float(celsius_entry.get())
    fahrenheit = celsius * 9/5 + 32
    fahrenheit_entry.delete(0, END)
    fahrenheit_entry.insert(0, fahrenheit)

convert_button = Button(window, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=2)

window.mainloop()
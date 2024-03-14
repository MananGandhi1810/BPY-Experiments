# Write a Python program that implements a temperature converter application using Tkinter, allowing users to convert between Celsius and Fahrenheit.

from tkinter import *

window = Tk()
window.title("Temperature Converter")
celsius_label = Label(window, text="Celsius:")
celsius_label.grid(row=0, column=0)
celsius_entry = Entry(window, width=10)
celsius_entry.grid(row=0, column=1)
fahrenheit_label = Label(window, text="Fahrenheit:")
fahrenheit_label.grid(row=1, column=0)
fahrenheit_entry = Entry(window, width=10)
fahrenheit_entry.grid(row=1, column=1)
def convert():
    if celsius_entry.get() != "":
        fahrenheit = (float(celsius_entry.get()) * 9/5) + 32
        fahrenheit_entry.delete(0, END)
        fahrenheit_entry.insert(0, str(fahrenheit))
    elif fahrenheit_entry.get() != "":
        celsius = (float(fahrenheit_entry.get()) - 32) * 5/9
        celsius_entry.delete(0, END)
        celsius_entry.insert(0, str(celsius))

convert_button = Button(window, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=2)
window.mainloop()
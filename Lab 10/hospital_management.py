from tkinter import Tk, Label, Entry, Button, Radiobutton, Frame, messagebox

window = Tk()
window.title("Hospital Management System")
window.geometry("400x200")
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
header = Label(window, text="Banyan Tree Hospital", font=("Inter", 20))
header.grid(row=0, column=0, columnspan=2)
name_label = Label(window, text="Name")
name_label.grid(row=1, column=0)
name_entry = Entry(window)
name_entry.grid(row=1, column=1)
age_label = Label(window, text="Age")
age_label.grid(row=2, column=0)
age_entry = Entry(window)
age_entry.grid(row=2, column=1)
gender_label = Label(window, text="Gender")
gender_label.grid(row=3, column=0)
gender_frame = Frame(window)
gender = "Male"
male_radio = Radiobutton(gender_frame, text="Male", value="Male", variable=gender)
male_radio.grid(row=0, column=0)
female_radio = Radiobutton(gender_frame, text="Female", value="Female", variable=gender)
female_radio.grid(row=0, column=1, padx=10)
gender_frame.grid(row=3, column=1)
location_label = Label(window, text="Location")
location_label.grid(row=4, column=0)
location_entry = Entry(window)
location_entry.grid(row=4, column=1)
phone_number_label = Label(window, text="Phone Number")
phone_number_label.grid(row=5, column=0)
phone_number_entry = Entry(window)
phone_number_entry.grid(row=5, column=1)


def clear():
    name_entry.delete(0, "end")
    age_entry.delete(0, "end")
    location_entry.delete(0, "end")
    phone_number_entry.delete(0, "end")


def onsubmit():
    name = name_entry.get()
    age = age_entry.get()
    location = location_entry.get()
    phone_number = phone_number_entry.get()
    if name == "" or age == "" or location == "" or phone_number == "":
        messagebox.showerror("Error", "Please fill all the fields")
        return
    if not age.isdigit():
        messagebox.showerror("Error", "Age should be a number")
        return
    if (
        len(phone_number.replace("+91 ", "").replace("+91", "")) != 10
        or not phone_number.isdigit()
    ):
        messagebox.showerror("Error", "Phone number should be a 10 digit number")
        return
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Location:", location)
    print("Phone Number:", phone_number)
    messagebox.showinfo("Success", "Appointment is confirmed")


clear_button = Button(window, text="Clear", command=clear)
clear_button.grid(row=6, column=0)
submit_button = Button(window, text="Submit", command=onsubmit)
submit_button.grid(row=6, column=1)
close_button = Button(window, text="Close", command=window.quit)
close_button.grid(row=7, column=0, columnspan=2)
window.mainloop()

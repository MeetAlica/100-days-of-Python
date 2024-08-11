from tkinter import *


def calculate():
    user_input = float(input.get())
    kilometer = round(user_input * 1.609344, 2)
    label_3.config(text=kilometer)

# Window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(300, 100)
window.config(padx=20, pady=20)

# Entry
input = Entry(width=10)
input.grid(column=2, row=1)
input.focus()

# Labels
label_1 = Label(text="Miles")
label_2 = Label(text="is equal to")
label_3 = Label(text="0", width=10)
label_4 = Label(text="Km")

label_1.grid(column=3, row=1)
label_2.grid(column=1, row=2)
label_3.grid(column=2, row=2)
label_4.grid(column=3, row=2)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)

window.mainloop()

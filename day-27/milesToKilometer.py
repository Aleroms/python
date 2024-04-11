from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=28, pady=28)


def button_clicked():
    try:
        miles = int(input.get())
        km = round(miles * 1.6)
        conversion_label.config(text=km)
    except:
        conversion_label.config(text="ERROR")


# Labels
miles_label = Label(text="Miles")
kilometer_label = Label(text="Km")
equality_label = Label(text="is equal to")
conversion_label = Label(text="0")
conversion_label.grid(column=1, row=1)
equality_label.grid(column=0, row=1)
miles_label.grid(column=2, row=0)
kilometer_label.grid(column=2, row=1)

# Inputs
input = Entry(width=10)
input.grid(column=1, row=0)

# Buttons
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()

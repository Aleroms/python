from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=500)
window.config(padx=28, pady=28)


def button_clicked():
    # my_label["text"] = "Button got clicked"
    # my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# creating a label
my_label = Label(text="I am a label", font=('Arial', 24, "bold"))
# make center of program
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0,row=0)
# my_label.pack()  # to insert onscreen must pack() it

# button
button = Button(text="Click Me", command=button_clicked)
button2 = Button(text="New Button", command=button_clicked)
button.grid(column=1, row=1)
button2.grid(column=2, row=0)
# button.pack()

# Entry
input = Entry(width=10)
input.grid(column=4, row=3)
# input.place(x=0, y=0)

# must be last line
window.mainloop()

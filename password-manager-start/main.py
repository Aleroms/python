from tkinter import *
from tkinter import messagebox
import PasswordGen
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = PasswordGen.generate()
    password_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    is_ok = validate()
    if not is_ok:
        return

    is_ok = confirm_inputs()

    if is_ok:
        with open("test.txt", "a") as f:
            text = f"{website_input.get()},{email_input.get()},{password_input.get()}\n"
            f.write(text)
            reset_fields()


def confirm_inputs():
    return messagebox.askokcancel(
        title=website_input.get(),
        message="is this okay to save?\n" + \
                f"Website: {website_input.get()}\n" + \
                f"Email: {email_input.get()}\n" + \
                f"Password: {password_input.get()}\n")


def validate():
    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave blank fields")
        return False
    return True


def reset_fields():
    website_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

# creating image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# creating labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# creating inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "example@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="W")

# creating buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
# 2 buttons: generate password, add

window.mainloop()

from tkinter import *
from tkinter import messagebox
import PasswordGen
import json


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
    new_data = {
        website_input.get(): {
            "email": email_input.get(),
            "password": password_input.get()
        }
    }

    if is_ok:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

        finally:
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


def search():
    # open data file
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            print(data[website_input.get()])
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="The file you requested does not exist")
    except KeyError:
        messagebox.showerror(title="No Match Found", message="No match found for provided input")
    else:
        current = data[website_input.get()]
        messagebox.showinfo(title=website_input.get(), message=f"Email:{current["email"]}\n" \
                                                               f"Password: {current["password"]}")
    # check to see if key exists
    # throw popup error if not found
    # else return email and password as popup


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
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "example@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

# creating buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")
# 2 buttons: generate password, add

window.mainloop()

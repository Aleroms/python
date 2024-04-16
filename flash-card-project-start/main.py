import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/chinese_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card)
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card_word, text=current_card["Chinese"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(width=800, height=526, padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# create canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="./images/card_back.png")
# canvas.create_image(400, 263, images=card_back_img)
canvas.grid(row=0, column=0, columnspan=2)

#create button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

corect_img = PhotoImage(file="./images/right.png")
correct_btn = Button(image=corect_img, highlightthickness=0, command=next_card)
correct_btn.grid(column=1, row=1)

next_card()
window.mainloop()

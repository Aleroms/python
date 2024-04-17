from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN_COLOR = "#78c1a3"
RED_COLOR = "#f38989"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # Score
        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 10, "bold")
        )
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="pls",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        self.true_btn = Button(
            image=true_img,
            highlightthickness=0,
            command=self.true_button
        )
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(
            image=false_img,
            highlightthickness=0,
            command=self.false_button
        )
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="No more questions left")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg=GREEN_COLOR)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg=RED_COLOR)
        self.window.after(1000, self.get_next_question)

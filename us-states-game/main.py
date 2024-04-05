import turtle
import pandas

# init game logic stuff
total_states = 50
correct_guesses = 0

# init Turtle stuff
screen = turtle.Screen()
screen.title("U.S. States Game")
imagePath = "./blank_states_img.gif"
screen.addshape(imagePath)
turtle.shape(imagePath)

# csv stuff
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    title = f"{len(guessed_states)}/{total_states} States Correct"
    prompt = "What's another state's name?"
    answer_state = screen.textinput(title=title, prompt=prompt).title()

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)

        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states not guessed by user

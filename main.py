import pandas as pd
from turtle import Turtle, Screen, textinput

screen = Screen()
pen = Turtle(visible=False)
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
pen.penup()
data = pd.read_csv("50_states.csv")

states = data["state"].tolist()


print(states)
answer = "xd"
correct = 0
while len(states) > 0 and answer != "exit":
    answer = textinput(f"{correct}/50 States Correct", "State name")

    if answer in states:
        correct += 1
        good = (data[data["state"] == answer]).values.flatten().tolist()
        pen.goto(good[1], good[2])
        pen.write(good[0])
        states.remove(answer)

final = pd.DataFrame(states)
final.to_csv("missed.csv")
screen.exitonclick()
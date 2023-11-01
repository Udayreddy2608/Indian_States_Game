import turtle
from turtle import Turtle,Screen
import pandas
screen=Screen()
image="india.gif"
screen.addshape(image)
turtle.shape(image)

states=pandas.read_csv("states.csv")
all_states=states["state"].tolist()
guessed_states=[]

while len(guessed_states)<29:
    answer = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Guess Next City").title()
    if answer=="Exit":
        screen.clear()
        me=Turtle()
        me.penup()
        me.color("Red")
        me.hideturtle()
        me.goto(-200,0)
        me.write(arg=f"Your Score is {len(guessed_states)}",font=("Courier",54,"normal"))
        break
    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        you=Turtle()
        you.hideturtle()
        you.penup()
        state_data=states[states.state==answer]
        you.goto(int(state_data.x),int(state_data.y))
        you.write(arg=answer,font=("Courier",14,"normal"))


screen.exitonclick()

from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=500,height= 400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a colour')

colours = ["red","orange","yellow","green","blue","purple"]
all_turtles = []
y_pos = [-150, -100, -50, 0 , 50, 100 ]

for turtle in range(0,6):
    turtle_name = Turtle(shape = "turtle")
    turtle_name.color(colours[turtle])
    turtle_name.penup()
    turtle_name.goto(x= -230, y= y_pos[turtle])
    all_turtles.append(turtle_name)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_colour = turtle.pencolor()
            print(f'The winner is {winning_colour}')
            if winning_colour.lower() == user_bet.lower():
                print('You win!')
            is_race_on= False
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()



# tim = Turtle(shape= "turtle")
# tim.penup()
# tim.color("red")
# tim.goto(x=-230, y = -100)


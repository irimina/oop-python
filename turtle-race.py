# Turtle race

# import turtle class, this is like a blue print for making a turtle
from turtle import Turtle
from random import randint

# create an instance of the turtle object and give it a name

laura = Turtle()
# julian is an int or string is a special kind of variable
# we need to give each turtle object a different name


# now let's tell the turtle object what it should look like
# inside the object are attributes which are pieces of data we can define


# turtle object has atributes for color and shape so let's customize these

laura.color('red')
laura.shape('turtle')


'''
We can also tell our Turtle object what to do by calling other methods.
With the code below, we are instructing the object to stop drawing with
penup(), then to move to a location with goto(),
and finally to get ready to draw a line with pendown().

'''

laura.penup()
laura.goto(-160, 100)
laura.pendown()


# YOUR TURN - create 3 more instances of the turtle object,
# each with a different name and a different starting point

jim=Turtle()
jim.color('blue')
jim.shape('turtle')
jim.penup()
jim.goto(-160, 70)
jim.pendown()


julian=Turtle()
julian.color('green')
julian.shape('turtle')
julian.penup()
julian.goto(-160, 40)
julian.pendown()

jessie=Turtle()
jessie.color('yellow')
jessie.shape('turtle')
jessie.penup()
jessie.goto(-160, 10)
jessie.pendown()


# let's meake the turtle objects race

for movement in range(100):
    laura.forward(randint(1,8))
    julian.forward(randint(1,8))
    jim.forward(randint(1,8))
    jessie.forward(randint(1,8))


#input("Press Enter to close")







from shapes import Triangle, Rectangle, Oval


# define the objects
rect1=Rectangle()
rect2= Rectangle()


# we use some setters ( = methods to set the attributes of the object)
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")

# call the object on the screen
rect1.draw()


# another instance of the class Rectangle, with 50 width,150 height, yellow
rect2.set_width(50)
rect2.set_width(150)
rect2.set_color("yellow")

# move the rect2 out of rect1
rect2.set_x(100)
rect2.set_y(100)

# call the object on the screen
rect2.draw()


#############################

oval1=Oval()
oval1.randomize()
oval1.draw()

#############################

tri=Triangle(5,5,100,5,100,200)
tri.draw()

'''
documentation to further customize
https://htmlpreview.github.io/?https://github.com/raspberrypilearning/shapes/blob/master/shapes.html

'''




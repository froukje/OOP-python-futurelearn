from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_width(100)
rect1.set_color("blue")

rect1.draw()

rect2 = Rectangle()
rect2.set_x(100)
rect2.set_y(100)
rect2.set_width(100)
rect2.set_width(50)
rect2.set_color("red")

rect2.draw()

oval = Oval()
oval.randomize()

oval.draw()


triangle = Triangle(5,5,100,100,200,100)
triangle.set_x(150)
triangle.set_y(250)
triangle.set_color("green")

triangle.draw()

paper.display()

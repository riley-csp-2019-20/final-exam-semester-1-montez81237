import turtle as trtl
# Make new turtles
m = trtl.Turtle()

# make turtle move
def m_up():
    m.setheading(90)
    m.forward(10)
def m_down():
    m.setheading(270)
    m.forward(10)
def m_left():
    m.setheading(180)
    m.forward(10)
def m_right(): 
    m.setheading(0)
    m.forward(10)


# Make the pensize bigger and smaller
def m_bpensize():
    m.pensize(5)
    
def m_spensize():
    m.pensize(1)
 
# make the keys move to the turtle
wn = trtl.Screen()
wn.onkeypress(m_up,"Up")
wn.onkeypress(m_down,"Down")
wn.onkeypress(m_left,"Left")
wn.onkeypress(m_right,"Right")
wn.onkeypress(m_bpensize,"P")
wn.onkeypress(m_spensize, "O")
wn.listen()
wn.mainloop()
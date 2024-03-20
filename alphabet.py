import turtle as t
import math

def circle(size):
    t.pendown()
    for i in range(50):
        t.forward(9.34*size)
        t.left(360/50)

def halfcirlce(size):
    t.pendown()
    for i in range(25):
        t.forward(9.34*size)
        t.right(180/25)

def backhalfcirlce(size):
    t.pendown()
    for i in range(25):
        t.forward(9.34*size)
        t.left(180/25)

def turtle_PASS(size):
    width = 60*size

    t.penup()
    t.forward(width)

def turtle_A(size):
    # parameters
    height = 160*size
    space = 20*size
    angle_rad = 1.3
    len_A = math.sin(angle_rad)*height
    len_lintel = 4*height*math.cos(angle_rad)/3

    # paint letter
    t.pendown()
    t.left(75)
    t.forward(len_A)
    t.right(180)
    t.forward(2*len_A/3)
    t.left(105)
    t.forward(len_lintel)
    t.left(105)
    t.forward(2*len_A/3)
    t.right(180)
    t.forward(len_A)

    # make space
    t.penup()
    t.left(75)
    t.forward(space)
    t.pendown()

def turtle_B(size):
    # parameters
    width = 60*size
    height = 150*size
    space = 20*size

    # paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(0.3*width)
    halfcirlce(size/2)
    t.right(180)
    halfcirlce(size/2)
    t.forward(0.3*width+10)

    # spacing
    t.penup()
    t.right(180)
    t.forward(width/2+0.3*width+10)
    t.forward(space)

def turtle_C(size):
    # parameters
    height = 150 * size
    space = 20 * size

    # paint
    t.penup()
    t.forward(height/2)
    t.pendown()
    t.right(180)
    halfcirlce(size)

    # spacing
    t.penup()
    t.right(90)
    t.forward(height)
    t.left(90)
    t.forward(space)

def turtle_D(size):
    # parametrs
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(0.3*width)
    halfcirlce(size)
    t.forward(0.3*width+10)

    # spacing
    t.penup()
    t.right(180)
    t.forward(height/2+space+10)

def turtle_E(size):
    # parametrs
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(180)
    t.forward(width)
    t.left(90)
    t.forward(height/2)
    t.left(90)
    t.forward(width)
    t.right(180)
    t.forward(width)
    t.left(90)
    t.forward(height/2)
    t.left(90)
    t.forward(width)

    # spacing
    t.penup()
    t.forward(space)

def turtle_F(size):
    # parametrs
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(180)
    t.forward(width)
    t.left(90)
    t.forward(height / 2)
    t.left(90)
    t.forward(width)


    #spacing
    t.penup()
    t.right(90)
    t.forward(height/2)
    t.left(90)
    t.forward(space)

def turtle_G(size):
    #parameters
    height = 150 * size
    space = 20* size

    #painting
    t.forward(75*size)
    t.left(90)
    t.forward(150*size)
    t.left(90)
    backhalfcirlce(size)
    t.left(90)
    t.forward(75*size*0.8)
    t.left(90)
    t.forward(20*size)

    #spacing
    t.penup()
    t.left(90)
    t.forward(75*size*0.8)
    t.left(90)
    t.forward(20*size)
    t.forward(space)

def turtle_H(size):
    #parameters
    height = 150 * size
    wight = 60 * size
    space = 20 * size

    #paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(180)
    t.forward(height/2)
    t.left(90)
    t.forward(wight)
    t.left(90)
    t.forward(height/2)
    t.right(180)
    t.forward(height)

    #spacing
    t.penup()
    t.left(90)
    t.forward(space)

def turtle_I(size):
    #parameters
    width = 60*size
    height = 150*size
    space = 20*size

    #paint letter I
    t.pendown()
    t.forward(width)
    t.right(180)
    t.forward(width/2)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.forward(width/2)
    t.right(180)
    t.forward(width)

    #spacing
    t.penup()
    t.right(90)
    t.forward(height)
    t.left(90)
    t.forward(space)

def turtle_J(size):
    #parameters
    height = 150 * size
    width = 60 * size
    space = 20 * size

    #paint
    t.pendown()
    t.forward(width/3)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width/2)
    t.left(90)
    t.forward(height/20)
    t.right(180)
    t.forward(height/20)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height/20)

    #spacing
    t.penup()
    t.forward(19*height/20)
    t.left(90)
    t.forward(space)

def turtle_K(size):
    #parameters
    width = 60 * size
    height = 150 * size

    #paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(180)
    t.forward(height/2)
    t.left(150)
    t.forward(height*0.55)
    t.right(180)
    t.forward(height*0.55)
    t.left(60)
    t.forward(height*0.55)
    t.left(180)
    t.forward(height*0.55)

    #spacing
    t.penup()
    t.left(150)
    t.forward(height/2)
    t.left(90)
    t.forward(height*0.8/2)

def turtle_L(size):
    #parameters
    height = 150 * size
    width = 60 * size
    space = 20 * size

    #paint
    t.penup()
    t.left(90)
    t.forward(height)
    t.pendown()
    t.left(180)
    t.forward(height)
    t.left(90)
    t.forward(width)

    #spacing
    t.penup()
    t.forward(space)

def turtle_M(size):
    #parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size
    #paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(150)
    t.forward(height/(2*math.cos(0.5235988)))
    t.left(120)
    t.forward(height/(2*math.cos(0.5235988)))
    t.right(150)
    t.forward(height)
    #spacing
    t.penup()
    t.left(90)
    t.forward(space)

def turtle_N(size):
    #parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    #paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(150)
    t.forward(height/(math.cos(0.5235988)))
    t.left(150)
    t.forward(height)
    t.left(180)
    t.forward(height)
    t.left(90)

    #spacing
    t.penup()
    t.forward(space)

def turtle_O(size):
    #parameters
    height = 150 * size
    width = 60 * size
    space = 20 * size

    #paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)

    # spacing
    t.right(180)
    t.penup()
    t.forward(width + space)


def turtle_P(size):
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(90)
    halfcirlce(size/2)

    # spacing
    t.penup()
    t.left(90)
    t.forward(height/2)
    t.left(90)
    t.forward(height/4)
    t.forward(space)

def turtle_Q(size):
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.penup()
    t.forward(height/2)
    t.pendown()
    circle(size)

    t.left(90)
    t.penup()
    t.forward(height/2)
    t.pendown()
    t.right(150)
    t.penup()
    t.forward(height/4)
    t.pendown()
    t.forward(height/2)

    # spacing
    t.penup()
    t.right(180)
    t.forward(3*height/4)
    t.left(150)
    t.forward(height/2)
    t.left(90)
    t.forward(height/2)
    t.forward(space)

def turtle_R(size): #WARNING Ряд букв понимается
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.pendown()
    t.left(90)
    t.forward(height)
    t.right(90)
    halfcirlce(size/2)
    t.right(180)
    t.right(60)
    t.forward(height/(2*math.cos(0.5235988)))

    # spacing
    t.penup()
    t.left(60)
    t.forward(space)

def turtle_S(size):
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.penup()
    t.forward(width)
    t.left(90)
    t.forward(height*0.9)

    t.pendown()
    t.forward(height*0.1)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height/2)
    t.left(90)
    t.forward(width)
    t.right(90)
    t.forward(height/2)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height*0.1)

    # spacing
    t.penup()
    t.right(180)
    t.forward(height*0.1)
    t.left(90)
    t.forward(width)
    t.forward(space)

def turtle_T(size):
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.penup()
    t.forward(width/2)
    t.pendown()
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width/2)
    t.left(180)
    t.forward(width)

    # spacing
    t.penup()
    t.right(90)
    t.forward(height)
    t.left(90)
    t.forward(space)

def turtle_U(size):
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.penup()
    t.left(90)
    t.forward(height)
    t.pendown()
    t.left(180)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)

    # spacing
    t.penup()
    t.right(180)
    t.forward(height)
    t.left(90)
    t.forward(space)

def turtle_V(size):
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.penup()
    t.left(90)
    t.forward(height)
    t.right(170)
    t.pendown()
    t.forward(height/math.cos(0.1745322925))
    t.left(160)
    t.forward(height/math.cos(0.1745322925))

    # spacing
    t.penup()
    t.right(170)
    t.forward(height)
    t.left(90)
    t.forward(space)

def turtle_W(size):
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.penup()
    t.left(90)
    t.forward(height)
    t.right(170)
    t.pendown()
    t.forward(height / math.cos(0.1745322925))
    t.left(160)
    t.forward(height / math.cos(0.1745322925))
    t.right(160)

    t.forward(height / math.cos(0.1745322925))
    t.left(160)
    t.forward(height / math.cos(0.1745322925))

    # spacing
    t.penup()
    t.right(170)
    t.forward(height)
    t.left(90)
    t.forward(space)

def turtle_X(size):
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.pendown()
    t.left(75)
    t.forward(height*math.sin(1.3088996))
    t.penup()
    t.left(105)
    t.forward(height*math.cos(1.3088996))
    t.pendown()
    t.left(105)
    t.forward(height*math.sin(1.3088996))

    # spacing
    t.penup()
    t.left(75)
    t.forward(space)

def turtle_Y(size):
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.penup()
    t.left(90)
    t.forward(height)
    t.pendown()
    t.right(145)
    t.forward(height/(3*math.cos(0.610865238)))
    t.left(110)
    t.forward(height / (3 * math.cos(0.610865238)))
    t.left(180)
    t.forward(height / (3 * math.cos(0.610865238)))
    t.left(35)
    t.forward(height*2/3)


    # spacing
    t.penup()
    t.left(90)
    t.forward(height / (6 * math.sin(0.610865238)))

def turtle_Z(size):
    # parametres
    height = 150 * size
    width = 60 * size
    space = 20 * size

    # paint
    t.penup()
    t.left(90)
    t.forward(height*0.9)
    t.pendown()
    t.forward(height*0.1)
    t.right(90)
    t.forward(width)
    t.right(105)
    t.forward(height*math.sin(1.3088996)+10*size)
    t.left(105)
    t.forward(width)
    t.left(90)
    t.forward(height*0.1)

    # spacing
    t.penup()
    t.left(180)
    t.forward(height*0.1)
    t.left(90)
    t.forward(space)

def turtleprint(string, size):
    string = string.upper()
    for letter in string:
        match letter:
            case "A": turtle_A(size)
            case "B": turtle_B(size)
            case "C": turtle_C(size)
            case "D": turtle_D(size)
            case "E": turtle_E(size)
            case "F": turtle_F(size)
            case "G": turtle_G(size)
            case "H": turtle_H(size)
            case "I": turtle_I(size)
            case "J": turtle_J(size)
            case "K": turtle_K(size)
            case "L": turtle_L(size)
            case "M": turtle_M(size)
            case "N": turtle_N(size)
            case "O": turtle_O(size)
            case "P": turtle_P(size)
            case "Q": turtle_Q(size)
            case "R": turtle_R(size)
            case "S": turtle_S(size)
            case "T": turtle_T(size)
            case "U": turtle_U(size)
            case "V": turtle_V(size)
            case "W": turtle_W(size)
            case "X": turtle_X(size)
            case "Y": turtle_Y(size)
            case "Z": turtle_Z(size)
            case " ": turtle_PASS(size)
import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	         tur.pu()
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.pd()
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(30)
    elif letter == "C":
	tur.pu() 
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(60)
        tur.left(90)
        tur.fd(50)
    elif letter == "D":
	tur.pu() 
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.pd()
        tur.left(90)
        tur.fd(70)
        tur.left(90)
        tur.circle(35,180)
    elif letter == "E":
	tur.pu() 
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.pd()
        tur.left(90)
        tur.fd(60)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        tur.left(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.pd()
        tur.fd(25)
        tur.pu()
        tur.left(180)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.pd()
        tur.fd(30)

    elif letter == "F":
	tur.pu() 
        tur.right(90)
        tur.fd(60)
        tur.right(90)
        tur.pd()
        tur.left(90)
        tur.fd(60)
        tur.pu()
        tur.right(180)
        tur.fd(30)
        tur.pd()
        tur.right(90)
        tur.fd(25)
        tur.pu()
        tur.right(180)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.pd()
        tur.fd(30)
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    	tur.left(45)
	tur.fd(40)
	tur.pu()
	tur.right(135)
	tur.fd(40)
	tur.pd()
	tur.right(135)
	tur.fd(65)
    elif letter == "X":
	tur.left(45)
	tur.fd(40)
	tur.pu()
	tur.right(135)
	tur.fd(40)
	tur.pd()
	tur.right(135)
	tur.fd(65)
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()

import turtle
import math

screenSize_X = 1248 #best size for grid 30*50. I found these number by try and error
screenSize_y = 864  #best size for grid 30*50. I found these number by try and error

myScreen = turtle
myScreen.speed(0)
myScreen.color("#000000") #background color to white
myScreen.hideturtle()
myScreen.Screen().title("Azin BFS Maze Solving Program")
myScreen.Screen().setup(width = screenSize_X,height = screenSize_y,startx=0, starty=0)  #setup the working screen

topLeft_x = -1*(screenSize_X /2) + 24 #shift X location to the new position
topLeft_y = (screenSize_y /2) - 24 #shift Y location to the new position

def DrawEmptyGrid(grid_row,grid_col):
    cellDim = 24
    myScreen.pensize(3)
    for row in range(0, grid_row+1):
        myScreen.penup()
        myScreen.goto(topLeft_x, topLeft_y - row * cellDim)
        myScreen.pendown()
        myScreen.goto(topLeft_x + grid_col * cellDim, topLeft_y - row * cellDim)

    for col in range(0, grid_col + 1):
        myScreen.penup()
        myScreen.goto(topLeft_x + col * cellDim, topLeft_y)
        myScreen.pendown()
        myScreen.goto(topLeft_x + col * cellDim, topLeft_y - grid_row * cellDim)

class GreenSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("green")
        self.shape("square")
        self.penup()
        self.speed(0)

def MazeTolist(grid_row,grid_col):
    for y in range(grid_row):  # read in the grid line by line
        for x in range(grid_col):
            xx = (x*24) + topLeft_x + 12
            yy = (y*24*-1) + topLeft_y - 12
            maze.append((xx,yy))

def text(message,x,y,size):
    FONT = ('calibry', size, 'bold')
    myScreen.penup()
    myScreen.goto(x,y)
    myScreen.write(message,align="left",font=FONT)

def guide():
    x = -588
    y = -300

    x += 0
    y -= 24+12
    text("*By left click in each cell of grid you can create walls. After finish maze design press [SPACE] button.", x,y, 10)

    x += 12
    y -= 12
    blue.goto(x,y)
    blue.stamp()
    text("Start Point", x + 14,y-8, 10)

    x += 110
    y -= 0
    red.goto(x,y)
    red.stamp()
    text("End Point", x + 14,y-8, 10)

    x += 110
    y -= 0
    gray.goto(x,y)
    gray.stamp()
    text("Walls", x + 14,y-8, 10)

    x += 110
    y -= 0
    green.goto(x,y)
    green.stamp()
    text("BFS visited", x + 14,y-8, 10)

    x += 110
    y -= 0
    yellow.goto(x,y)
    yellow.stamp()
    text("Back-track path", x + 14,y-8, 10)

def get_mouse_click_coor(x, y):
    turtle.onscreenclick(None)
    # Adjustancy
    adj_X = math.floor((x) / 24) * 24 + 12  # math.floor((x//((x//100)*100))+topLeft_x+12)#(math.floor(x//-400)+topLeft_x)
    adj_Y = math.floor( (y) / 24) * 24 + 12  # math.floor((y//((y//100)*100))+topLeft_y-12)#(math.floor(y//600)+topLeft_y)
    print(adj_X, adj_Y)
    if (adj_X, adj_Y) in maze and (adj_X, adj_Y) not in walls:  # check the cell down
        #print(adj_X, adj_Y)
        walls.append((adj_X, adj_Y))  # add coordinate to walls list
        gray.goto(adj_X, adj_Y)  # send green sprite to screen location
        gray.stamp()
        #print(walls)
    #print(x, y)
    myScreen.getscreen().update()
    turtle.onscreenclick(get_mouse_click_coor)

class GraySquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("gray")
        self.shape("square")
        self.penup()
        self.speed(0)

class BlueSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("blue")
        self.shape("square")
        self.penup()
        self.speed(0)

class RedSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.shape("square")
        self.penup()
        self.speed(0)

class YellowSquare(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("yellow")
        self.shape("square")
        self.penup()
        self.speed(0)


#init list
maze = []
walls = []

#init colour square
green = GreenSquare()
gray  = GraySquare()
yellow = YellowSquare()
red = RedSquare()
blue = BlueSquare()

#Get input m*n from user
grid_row =  int(myScreen.Screen().numinput("Draw Maze", "Please Set your Rows number:", 30, minval=1, maxval=30)) #Get [m] count grid rows from user
grid_col =  int(myScreen.Screen().numinput("Draw Maze", "Please Set your Columns number:", 50, minval=1, maxval=50)) #Get [n] count grid columns from user


+######  run!!! ############
DrawEmptyGrid(grid_row,grid_col)
MazeTolist(grid_row, grid_col)

# Show Start point
blue.goto(-588, 396)
blue.stamp()

# Show End point
red.goto((maze[-1]))
red.stamp()

guide()

def main():
    turtle.listen()
    turtle.onscreenclick(get_mouse_click_coor) #get walls from user
    turtle.mainloop()#get loop for more wall

def exit():
    myScreen.Screen().exitonclick()

main()
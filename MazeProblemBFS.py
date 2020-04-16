import turtle

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

grid_row =  int(myScreen.Screen().numinput("Draw Maze", "Please Set your Rows number:", 30, minval=1, maxval=30)) #Get [m] count grid rows from user
grid_col =  int(myScreen.Screen().numinput("Draw Maze", "Please Set your Columns number:", 50, minval=1, maxval=50)) #Get [n] count grid columns from user

DrawEmptyGrid(grid_row,grid_col)
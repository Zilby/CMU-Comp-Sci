#Lab 5 for Kesden

solved=False

class NoStartError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

def findStart(maze):
    x=0
    y=0
    for line in maze:
        for letter in line:
            if(letter=='S'):
                return [x,y]
            y+=1
        y=0
        x+=1
    raise NoStartError("No Start")

def findMax(l):
    output=-1
    for each in l:
        output+=1
    return output

def mazeSolver(maze,path):
    try:
        global start
        start=findStart(maze)
        maxx=findMax(maze)
        maxy=findMax(maze[0])
        maze[start[0]][start[1]]='P'
        return solveHelper(maze,start[0],start[1],maxx,maxy,path)
    except NoStartError:
        print "No starting point found"

def solveHelper(maze,x,y,maxx,maxy,stack):
    global solved
    global steps
    if(steps):
        print mazePrinter(maze)  
    if(solved!=True and x<=maxx and y<=maxy):
        if(maze[x][y]=='F'):
            solved=True
            global start
            global mazeSolution
            maze[start[0]][start[1]]='S'
            mazeSolution=maze
            stack.insert(0,[y,x])
            return True
        elif(maze[x][y]=='P'and x>=0 and y>=0):
            maze[x][y]='@'
            up=solveHelper(maze,x,y+1,maxx,maxy,stack)
            down=solveHelper(maze,x-1,y,maxx,maxy,stack)
            right=solveHelper(maze,x+1,y,maxx,maxy,stack)
            left=solveHelper(maze,x,y-1,maxx,maxy,stack)
            directions=[up,down,left,right]
            for each in directions:
                if(each==True):
                    stack.insert(0,[y,x])
                    return each
            if(solved!=True):
                maze[x][y]='P'
    return False

def mazePrinter(maze):
    output=""
    for line in maze:
        for letter in line:
            output+=str(letter)+" "
        output+="\n"
    return output

# This function reads a maze file, filename, and creates a maze, m.
# Please declare "m" as a list before calling the function and then pass it in. 
def readMaze(m, filename):
  mazeFile = open(filename, "r")
  lines = mazeFile.readlines()
  for line in lines:
    line = line.strip()
    row = [c for c in line]
    m.append(row)

start=[]
mazeFile = raw_input("Enter maze file name (sampleMaze.txt is the default, hardMaze.txt is harder) ")
step = raw_input("Would you like to see each individual step? (Enter 'yes' if interested) ")
steps=False
if(step=="yes"):
    steps=True
maze = []  # This declares the maze as an empty list
readMaze(maze, mazeFile) # This reads the maze into the list
print "\n"+mazePrinter(maze) # This prints the maze, showing it with the usual notation as a "list of lists"
mazeSolution = []
path=[]
if (mazeSolver(maze,path)):
    print mazePrinter(mazeSolution)
    print path
    print "*Note, maze treated like an array with 0's referring to the first row/column"
else:
    print "No solution found."

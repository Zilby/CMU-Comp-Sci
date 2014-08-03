#Tetris lab para la clase de Kesden

from Tkinter import *
import random

def run(rows,cols):
    root=Tk()
    global canvas
    canvas=Canvas(root,width=(cols*40)+100,height=(rows*40)+100,bg="white")
    canvas.pack()
    root.resizable(width=0,height=0)
    class Struct: pass
    canvas.data=Struct()
    canvas.data.rows=rows
    canvas.data.cols=cols
    root.bind("<Key>", keyPressed)
    init()
    timerFired()
    root.mainloop()

def init():
    canvas.data.cellDimension=40
    canvas.board=[]
    canvas.bg="white"
    for row in range(canvas.data.rows):
        canvas.board += [["blue"]*canvas.data.cols]
    iPiece = [[ True,  True,  True,  True]]
    jPiece = [[ True,  False, False],
              [ True,  True,  True]]
    lPiece = [[ False, False, True],
              [ True,  True,  True]]
    oPiece = [[ True,  True],
              [ True,  True]]
    sPiece = [[ False, True, True],
              [ True,  True, False]]
    tPiece = [[ False, True, False],
              [ True,  True, True]]
    zPiece = [[ True,  True, False],
              [ False, True, True]]
    tetrisPieces = [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]
    tetrisPieceColors = ["red", "yellow", "magenta", "pink", "cyan", "green", "orange"]
    canvas.data.tetrisPieces = tetrisPieces
    canvas.data.tetrisPieceColors = tetrisPieceColors
    canvas.data.fallingPiece=[[]]
    canvas.data.fallingPieceColor=""
    canvas.data.fallingPieceRow=0
    canvas.data.fallingPieceCol=0
    canvas.data.fallingPieceCols=0
    canvas.data.fallingPieceRows=0
    newFallingPiece()

def newFallingPiece():
    indexNum=random.randint(0,6)
    canvas.data.fallingPiece=canvas.data.tetrisPieces[indexNum]
    canvas.data.fallingPieceColor=canvas.data.tetrisPieceColors[indexNum]
    canvas.data.fallingPieceRow=0
    canvas.data.fallingPieceRows=len(canvas.data.fallingPiece)
    canvas.data.fallingPieceCols=len(canvas.data.fallingPiece[0])
    canvas.data.fallingPieceCol=(canvas.data.cols/2)-(canvas.data.fallingPieceCols/2)

def redrawAll():
    canvas.delete(ALL)
    drawGame()
    drawFallingPiece()
    #newFallingPiece()

def timerFired():
    redrawAll()
    canvas.after(50,timerFired)

def drawGame():
    '''
    # pre-load a few cells with known colors for testing purposes
    canvas.board[0][0] = "red" # top-left is red
    canvas.board[0][cols-1] = "white" # top-right is white
    canvas.board[rows-1][0] = "green" # bottom-left is green
    canvas.board[rows-1][cols-1] = "gray" # bottom-right is gray
    printBoard()
    '''
    drawBoard()

def drawBoard():
    for col in range(canvas.data.cols):
        for row in range(canvas.data.rows):
            #canvas.board[row][col]="blue"
            drawCell(row,col,canvas,canvas.board[row][col])

def drawFallingPiece():
    row=canvas.data.fallingPieceRow
    col=canvas.data.fallingPieceCol
    for vList in canvas.data.fallingPiece:
        for block in vList:
            if(block==True):
                drawCell(row,col,canvas,canvas.data.fallingPieceColor)
                #canvas.board[row][col]=canvas.data.fallingPieceColor
            col+=1
        col=canvas.data.fallingPieceCol
        row+=1
            

def drawCell(row,col,canvas,color):
    x1 = (col*canvas.data.cellDimension)+50
    y1 = (row*canvas.data.cellDimension)+50
    x2 = x1 + canvas.data.cellDimension
    y2 = y1 + canvas.data.cellDimension
    canvas.create_rectangle(x1,y1,x2,y2,fill="black",width=0)
    x1 = (col*canvas.data.cellDimension)+55
    y1 = (row*canvas.data.cellDimension)+55
    x2 = x1 + canvas.data.cellDimension-10
    y2 = y1 + canvas.data.cellDimension-10
    canvas.create_rectangle(x1,y1,x2,y2,fill=color,width=0)

def moveFallingPiece(drow,dcol):
    canvas.data.fallingPieceRow=canvas.data.fallingPieceRow+drow
    canvas.data.fallingPieceCol=canvas.data.fallingPieceCol+dcol
    if(fallingPieceIsLegal()==False):
        canvas.data.fallingPieceRow=canvas.data.fallingPieceRow-drow
        canvas.data.fallingPieceCol=canvas.data.fallingPieceCol-dcol
    

def fallingPieceIsLegal():
    row=canvas.data.fallingPieceRow
    col=canvas.data.fallingPieceCol
    for vList in canvas.data.fallingPiece:
        for block in vList:
            if(block==True):
                if(row>canvas.data.rows-1 or row<0 or
                   col>canvas.data.cols-1 or col<0 or
                   canvas.board[row][col]!="blue"):
                    return False
            col+=1
        col=canvas.data.fallingPieceCol
        row+=1
    return True

def rotateFallingPiece():
    tempPiece=canvas.data.fallingPiece
    tempDimensions=[canvas.data.fallingPieceRows,canvas.data.fallingPieceCols]
    tempLocation=[canvas.data.fallingPieceRow,canvas.data.fallingPieceCol]
    print "Location: Row: "+str(tempLocation[0])+" Col: "+str(tempLocation[1])
    #print "Dimensions: Rows: "+str(tempDimensions[0])+" Cols: "+str(tempDimensions[1])
    canvas.data.fallingPieceRows=tempDimensions[1]
    canvas.data.fallingPieceCols=tempDimensions[0]
    canvas.data.fallingPieceCol+=tempDimensions[1]-(tempDimensions[0]/2)
    canvas.data.fallingPiece=[]
    count=0
    while(count<tempDimensions[1]):
        x=[]
        for each in tempPiece:
            x+=[each[count]]
        canvas.data.fallingPiece+=[x]
        count+=1
    if(fallingPieceIsLegal==False):
        canvas.data.fallingPiece=tempPiece
        canvas.data.fallingPieceRows=tempDimensions[0]
        canvas.data.fallingPieceCols=tempDimensions[1]
        canvas.data.fallingPieceRow=tempLocation[0]
        canvas.data.fallingPieceCol=tempLocation[1]

def printBoard():
    print "["
    for col in canvas.board:
        print "[",
        for each in col:
            print each,
        print "]",
        print "\n"
    print "]"


def keyPressed(event):
    if(event.keysym=='Left'):
        moveFallingPiece(0,-1)
    elif(event.keysym=='Right'):
        moveFallingPiece(0,1)
    elif(event.keysym=='Down'):
        moveFallingPiece(1,0)
    elif(event.char==' '):
        rotateFallingPiece()
    #elif(event.keysym=='Up'):
        #moveFallingPiece(-1,0)
    else:   
        newFallingPiece()
        redrawAll()
        #printBoard()


run(15,10)

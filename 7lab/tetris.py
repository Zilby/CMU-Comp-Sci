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
    init()
    redrawAll()
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
    newFallingPiece()

def newFallingPiece():
    indexNum=random.randint(0,6)
    canvas.data.fallingPiece=canvas.data.tetrisPieces[indexNum]
    canvas.data.fallingPieceColor=canvas.data.tetrisPieceColors[indexNum]
    canvas.data.fallingPieceRow=0
    canvas.data.fallingPieceCols=len(canvas.data.fallingPiece[0])
    canvas.data.fallingPieceCol=(canvas.data.cols/2)-(canvas.data.fallingPieceCols/2)

def redrawAll():
    drawGame()
    drawFallingPiece()
    canvas.after(50,redrawAll)

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
            drawCell(row,col,canvas,canvas.board[row][col])

def drawFallingPiece():
    row=canvas.data.fallingPieceRow
    col=canvas.data.fallingPieceCol
    for vList in canvas.data.fallingPiece:
        for block in vList:
            if(block==True):
                drawCell(row,col,canvas,canvas.data.fallingPieceColor)
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
  # for now, for testing purposes, just choose a new falling piece
  # whenever ANY key is pressed!
  canvas = event.widget.canvas
  newFallingPiece()
  redrawAll()

run(15,10)

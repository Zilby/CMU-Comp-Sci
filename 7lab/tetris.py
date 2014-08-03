#Tetris lab para la clase de Kesden

#Extra Features:
#-game will speed up over time
#-drop piece feature added with prompt on first game before doing so (spacebar)
#-wiggle room added (when placing a piece regularly, there will be some time before it locks into place
#-pause feature added (p)


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
    canvas.data.first=True
    root.bind("<Key>", keyPressed)
    init()
    timerFired()
    root.mainloop()

def init():
    canvas.data.cellDimension=40
    canvas.board=[]
    canvas.bg="white"
    canvas.data.timer=20
    canvas.data.speed=20
    canvas.data.speedTimer=300
    canvas.data.placeTimer=2
    canvas.data.isGameOver=False
    canvas.data.pause=False
    canvas.data.score=0
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
    canvas.data.fallingPieceOrientation="up"
    newFallingPiece()

def newFallingPiece():
    indexNum=random.randint(0,6)
    canvas.data.fallingPiece=canvas.data.tetrisPieces[indexNum]
    canvas.data.fallingPieceColor=canvas.data.tetrisPieceColors[indexNum]
    canvas.data.fallingPieceRow=0
    canvas.data.fallingPieceRows=len(canvas.data.fallingPiece)
    canvas.data.fallingPieceCols=len(canvas.data.fallingPiece[0])
    canvas.data.fallingPieceCol=(canvas.data.cols/2)-(canvas.data.fallingPieceCols/2)
    canvas.data.fallingPieceOrientation="up"

def redrawAll():
    canvas.delete(ALL)
    drawGame()
    drawFallingPiece()


def timerFired():
    if(canvas.data.isGameOver==False and canvas.data.pause==False):
        redrawAll()
        canvas.data.timer-=1
        canvas.data.speedTimer-=1
        if(canvas.data.speedTimer==0 and canvas.data.speed!=5):
            canvas.data.speedTimer=300
            canvas.data.speed-=1
        if(canvas.data.timer==0):
            fell=moveFallingPiece(1,0)
            if(fell!=True):
                if(canvas.data.placeTimer==0):
                    placeFallingPiece()
                    removeFullRows()
                    newFallingPiece()
                    if(fallingPieceIsLegal()==False):
                        canvas.data.isGameOver=True
                else:
                    canvas.data.placeTimer-=1
            canvas.data.timer=canvas.data.speed
    elif(canvas.data.isGameOver==True):
        drawGameOver()
    canvas.after(25,timerFired)

def drawGame():
    canvas.create_text(20, 30, anchor=W, font="Fixedsys",text="Score: "+str(canvas.data.score))
    if(canvas.data.first==True):
        canvas.create_text((canvas.data.cols*20)-35, (canvas.data.rows*40)+75, anchor=W, font="Fixedsys",text="Press Space to Drop")
    drawBoard()

def drawGameOver():
    canvas.delete(ALL)
    canvas.create_rectangle(20,20,(canvas.data.cols*40)+80,(canvas.data.rows*40)+80,fill="red",width=0)
    canvas.create_text((canvas.data.cols*20)-5, (canvas.data.rows*20), anchor=W, font="Fixedsys",text="Game Over")
    canvas.create_text((canvas.data.cols*20)+10, (canvas.data.rows*20)+30, anchor=W, font="Fixedsys",text="Score: "+str(canvas.data.score))
    canvas.create_text((canvas.data.cols*20)-35, (canvas.data.rows*20)+60, anchor=W, font="Fixedsys",text="Press R to Restart")

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
            
def placeFallingPiece():
    row=canvas.data.fallingPieceRow
    col=canvas.data.fallingPieceCol
    for vList in canvas.data.fallingPiece:
        for block in vList:
            if(block==True):
                canvas.board[row][col]=canvas.data.fallingPieceColor
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
        if(drow==1):
            return False
    if(drow==1):
        canvas.data.placeTimer=2
    return True
    

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

def removeFullRows():
    fullRows=0
    full=True
    oldRow=canvas.data.rows
    newRow=canvas.data.rows-1
    for index in reversed(range(0,oldRow)):
        for row in [canvas.board[index]]:
            for block in row:
                if(block=="blue"):
                    full=False
            if(full==False):
                for index in range(0,canvas.data.cols):
                    canvas.board[newRow][index]=row[index]
                newRow-=1
            else:
                fullRows+=1
            full=True
    for indexR in range(0,newRow+1):
        for indexC in range(0,canvas.data.cols):
            canvas.board[indexR][indexC]="blue"
    canvas.data.score+=fullRows**2

def rotateFallingPiece(): #the rotato es dificil
    tempPiece=canvas.data.fallingPiece
    tempDimensions=[canvas.data.fallingPieceRows,canvas.data.fallingPieceCols]
    tempLocation=[canvas.data.fallingPieceRow,canvas.data.fallingPieceCol]
    canvas.data.fallingPieceRows=tempDimensions[1]
    canvas.data.fallingPieceCols=tempDimensions[0]
    dRowColTemp=[tempDimensions[1]-tempDimensions[0],tempDimensions[0]-tempDimensions[1]]
    dRowCol=[]
    for each in dRowColTemp: 
        if(each>0):
            each=(each/2)+1
        else:
            each=each/2
        dRowCol.append(each)
    if(canvas.data.fallingPieceOrientation=="up"):
        canvas.data.fallingPieceOrientation="right"
    elif(canvas.data.fallingPieceOrientation=="right"):
        canvas.data.fallingPieceOrientation="down"
    elif(canvas.data.fallingPieceOrientation=="down"):
        if(tempDimensions[0]!=tempDimensions[1]):
            dRowCol[1]+=1
        canvas.data.fallingPieceOrientation="left"
    elif(canvas.data.fallingPieceOrientation=="left"):
        if(tempDimensions[0]!=tempDimensions[1]):
            dRowCol[1]-=1
        canvas.data.fallingPieceOrientation="up"
    canvas.data.fallingPieceRow-=dRowCol[0]
    canvas.data.fallingPieceCol-=dRowCol[1]
    canvas.data.fallingPiece=[]
    count=0
    while(count<tempDimensions[1]):
        x=[]
        for each in tempPiece:
            x=[each[count]]+x
        canvas.data.fallingPiece+=[x]
        count+=1
    if(fallingPieceIsLegal()==False):
        canvas.data.fallingPiece=tempPiece
        canvas.data.fallingPieceRows=tempDimensions[0]
        canvas.data.fallingPieceCols=tempDimensions[1]
        canvas.data.fallingPieceRow=tempLocation[0]
        canvas.data.fallingPieceCol=tempLocation[1]
        if(canvas.data.fallingPieceOrientation=="up"):
            canvas.data.fallingPieceOrientation="left"
        elif(canvas.data.fallingPieceOrientation=="left"):
            canvas.data.fallingPieceOrientation="down"
        elif(canvas.data.fallingPieceOrientation=="down"):
            canvas.data.fallingPieceOrientation="right"
        elif(canvas.data.fallingPieceOrientation=="right"):
            canvas.data.fallingPieceOrientation="up"

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
    if(canvas.data.pause==False):
        if(event.keysym=='Left'):
            moveFallingPiece(0,-1)
        elif(event.keysym=='Right'):
            moveFallingPiece(0,1)
        elif(event.keysym=='Down'):
            moveFallingPiece(1,0)
        elif(event.keysym=='Up'):
            rotateFallingPiece()
        elif(event.char==' '):
            canvas.data.first=False
            while(moveFallingPiece(1,0)):
                moveFallingPiece(1,0)
                canvas.data.placeTimer=0
        #elif(event.keysym=='Up'):
            #moveFallingPiece(-1,0)
        #elif(event.char=='n'):   
            #newFallingPiece()
            #redrawAll()
        elif(event.char=='r'):   
            init()
    if(event.char=='p'):   
        if(canvas.data.pause==True):
            canvas.data.pause=False
        else:
            canvas.data.pause=True



run(15,10)

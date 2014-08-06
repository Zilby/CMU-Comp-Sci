#Final Project!!!!!

from Tkinter import *

def run():
    root=Tk()
    global canvas
    canvas=Canvas(root,width=500,height=500,bg="white")
    canvas.pack()
    root.resizable(width=0,height=0)
    class Struct: pass
    canvas.data=Struct()
    canvas.data.first=True
    root.bind("<Key>", keyPressed)
    init()
    timerFired()
    root.mainloop()

def init():
    canvas.bg="white"
    canvas.data.timer=20
    canvas.data.isGameOver=False
    canvas.data.pause=False
    canvas.data.score=0

def timerFired():
    if(canvas.data.isGameOver==False and canvas.data.pause==False):
        redrawAll()
        #canvas.data.timer-=1
        #if(canvas.data.timer==0):
    elif(canvas.data.isGameOver==True):
        drawGameOver()
    canvas.after(25,timerFired)

def redrawAll():
    canvas.delete(ALL)
    drawGame()

def drawGame():
    canvas.create_text(20, 30, anchor=W, font="Fixedsys",text="Score: "+str(canvas.data.score))

def drawGameOver():
    canvas.delete(ALL)
    canvas.create_rectangle(20,20,(canvas.data.cols*40)+80,(canvas.data.rows*40)+80,fill="red",width=0)
    canvas.create_text((canvas.data.cols*20)-5, (canvas.data.rows*20), anchor=W, font="Fixedsys",text="Game Over")
    canvas.create_text((canvas.data.cols*20)+10, (canvas.data.rows*20)+30, anchor=W, font="Fixedsys",text="Score: "+str(canvas.data.score))
    canvas.create_text((canvas.data.cols*20)-35, (canvas.data.rows*20)+60, anchor=W, font="Fixedsys",text="Press R to Restart")

def keyPressed(event):
    if(event.char=='p'):   
        if(canvas.data.pause==True):
            canvas.data.pause=False
        else:
            canvas.data.pause=True
    #if(canvas.data.pause==False):
        '''if(event.keysym=='Left'):
        elif(event.keysym=='Right'):
        elif(event.keysym=='Down'):
        elif(event.keysym=='Up'):
        elif(event.char==' '):
        elif(event.char=='r'):   
            init()'''
    

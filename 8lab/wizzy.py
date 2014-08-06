#Final Project!!!!!

from Tkinter import *

def run():
    root=Tk()
    global canvas
    canvas=Canvas(root,width=600,height=600,bg='#%02x%02x%02x' % (35, 0, 61))
    canvas.pack()
    root.resizable(width=0,height=0)
    class Struct: pass
    canvas.data=Struct()
    canvas.data.first=True
    root.bind("<Key>", keyPressed)
    root.bind("<KeyRelease>", keyReleased)
    init()
    timerFired()
    root.mainloop()

def init():
    canvas.data.bg='#%02x%02x%02x' % (35, 0, 61)
    canvas.data.timer=20
    canvas.data.isGameOver=False
    canvas.data.isTitle=True
    canvas.data.pause=False
    canvas.data.score=0
    canvas.data.level=0
    canvas.data.nextLevel=True
    canvas.data.alive=True
    canvas.data.lives=10
    canvas.data.pxcorL=0
    canvas.data.pxcorR=0
    canvas.data.pycorU=0
    canvas.data.pycorD=0
    canvas.data.facing="right"
    canvas.data.jumping=False
    canvas.data.attacking=False
    canvas.data.speedH=0
    canvas.data.speedV=0
    canvas.data.animationTimer=3
    canvas.data.still=True
    canvas.data.platforms=[]
    canvas.data.enemy1s=[]
    canvas.data.enemy2s=[]
    canvas.data.projectiles=[]
    canvas.data.projectileRs=[]
    canvas.data.attackL=PhotoImage(file="attackL.gif")
    canvas.data.attackR=PhotoImage(file="attackR.gif")
    canvas.data.Enemy1L=PhotoImage(file="Enemy1L.gif")
    canvas.data.Enemy1R=PhotoImage(file="Enemy1R.gif")
    canvas.data.Enemy2L=PhotoImage(file="Enemy2L.gif")
    canvas.data.Enemy2R=PhotoImage(file="Enemy2R.gif")
    canvas.data.jumpL=PhotoImage(file="jumpL.gif")
    canvas.data.jumpR=PhotoImage(file="jumpR.gif")
    canvas.data.projectileEL=PhotoImage(file="projectileEL.gif")
    canvas.data.projectileER=PhotoImage(file="projectileER.gif")
    canvas.data.projectileL=PhotoImage(file="projectileL.gif")
    canvas.data.projectileR=PhotoImage(file="projectileR.gif")
    canvas.data.stillL=PhotoImage(file="stillL.gif")
    canvas.data.stillR=PhotoImage(file="stillR.gif")
    canvas.data.Title=PhotoImage(file="Title.gif")
    canvas.data.walkL=PhotoImage(file="walkL.gif")
    canvas.data.walkR=PhotoImage(file="walkR.gif")



def timerFired():
    if(canvas.data.isGameOver==False and 
       canvas.data.pause==False and 
       canvas.data.isTitle==False):
        redrawAll()
        movePlayer()
        #canvas.data.timer-=1
        #if(canvas.data.timer==0):
    elif(canvas.data.isGameOver==True):
        drawGameOver()
    elif(canvas.data.isTitle==True):
        drawTitle()
    elif(canvas.data.pause==True):
        canvas.create_text(300, 280, font="Fixedsys",text="Paused ",fill="black")
    canvas.after(25,timerFired)

def redrawAll():
    canvas.delete(ALL)
    drawGame()

def drawGame():
    canvas.create_rectangle(0,540,600,600,fill="black")
    canvas.create_text(20, 560, anchor=NW, font="Fixedsys",text="Score: "+str(canvas.data.score),fill="white")
    canvas.create_text(120, 560, anchor=NW, font="Fixedsys",text="Lives: "+str(canvas.data.lives),fill="red")
    canvas.create_text(510, 560, anchor=NW, font="Fixedsys",text="Level: "+str(canvas.data.level),fill="blue")
    drawLevel(canvas.data.level)

def drawLevel(level):
    for platform in canvas.data.platforms[1:]:
        canvas.create_rectangle(platform[2],platform[0],platform[3],platform[1],fill="grey")
    if(level==0):
        if(canvas.data.nextLevel==True):
            canvas.data.level=1
            canvas.data.nextLevel=False
            canvas.data.facing="right"
            canvas.data.attacking=False
            canvas.data.jumping=False
            canvas.data.still=True
            canvas.data.pxcorL=50
            canvas.data.pxcorR=canvas.data.pxcorL+30
            canvas.data.pycorD=540
            canvas.data.pycorU=canvas.data.pycorD-40
            canvas.data.platforms=[[540,600,0,600],[470,500,300,400]]
    elif(level==1):
        if(canvas.data.nextLevel==True):
            canvas.data.level=2
        else:
            playerImage=0
            if(canvas.data.facing=="right"):
                if(canvas.data.attacking==True):
                    playerImage=canvas.data.attackR
                elif(canvas.data.jumping==True):
                    playerImage=canvas.data.jumpR
                elif(canvas.data.still==False):
                    playerImage=canvas.data.walkR
                else:
                    playerImage=canvas.data.stillR
            else:
                if(canvas.data.attacking==True):
                    playerImage=canvas.data.attackL
                elif(canvas.data.jumping==True):
                    playerImage=canvas.data.jumpL
                elif(canvas.data.still==False):
                    playerImage=canvas.data.walkL
                else:
                    playerImage=canvas.data.stillL
            canvas.create_image(canvas.data.pxcorL-5,canvas.data.pycorD,anchor=SW,image=playerImage)

def drawTitle():
    canvas.delete(ALL)
    canvas.create_image(0,0,anchor=NW,image=canvas.data.Title)

def drawGameOver():
    canvas.delete(ALL)
    canvas.create_rectangle(20,20,(canvas.data.cols*40)+80,(canvas.data.rows*40)+80,fill="red",width=0)
    canvas.create_text((canvas.data.cols*20)-5, (canvas.data.rows*20), anchor=W, font="Fixedsys",text="Game Over")
    canvas.create_text((canvas.data.cols*20)+10, (canvas.data.rows*20)+30, anchor=W, font="Fixedsys",text="Score: "+str(canvas.data.score))
    canvas.create_text((canvas.data.cols*20)-35, (canvas.data.rows*20)+60, anchor=W, font="Fixedsys",text="Press R to Restart")

def movePlayer():
    if(canvas.data.speedH!=0):
        if(touchingPWall()==False):
            if((canvas.data.speedH>0 and canvas.data.pxcorR>=598)!=True and 
               (canvas.data.speedH<0 and canvas.data.pxcorL<=2)!=True):
                canvas.data.pxcorL+=canvas.data.speedH
                canvas.data.pxcorR+=canvas.data.speedH
                if(canvas.data.jumping==False):
                    if(touchingGround()==False):
                        canvas.data.jumping=True
                    else:
                        if(canvas.data.animationTimer==0):
                            canvas.data.animationTimer=3
                            if(canvas.data.still==True):
                                canvas.data.still=False
                            else:
                                canvas.data.still=True
                        else:
                            canvas.data.animationTimer-=1
            else:
                canvas.data.still=True
                canvas.data.animationTimer=3
            touchingPWall()
    else:
        if(canvas.data.jumping==False):
            canvas.data.still=True
    if(canvas.data.jumping==True):
        if(touchingGround()==False):
            for platform in canvas.data.platforms:
                if(canvas.data.pycorU<=platform[1]and
                   canvas.data.pycorU>=platform[0]and
                   canvas.data.pxcorR>platform[2]and 
                   canvas.data.pxcorL<platform[3]and 
                   canvas.data.speedV>0):
                    canvas.data.speedV=0
            canvas.data.pycorD-=canvas.data.speedV
            canvas.data.pycorU-=canvas.data.speedV
            canvas.data.speedV-=1
            touchingGround()
        else:
            canvas.data.jumping=False
            canvas.data.speedV=0
                

def touchingGround():
    isTouching=False
    for platform in canvas.data.platforms:
        if(canvas.data.pycorD>=platform[0]and 
           canvas.data.pycorD+canvas.data.speedV<=platform[0]and
           canvas.data.pxcorR>platform[2]and 
           canvas.data.pxcorL<platform[3]):
            canvas.data.pycorD=platform[0]
            canvas.data.pycorU=platform[0]-40
            isTouching=True
    return isTouching

def touchingPWall():
    isTouching=False
    for platform in canvas.data.platforms:
        if(((canvas.data.pxcorR>=platform[2]and canvas.data.pxcorR-canvas.data.speedH<=platform[2])or
           (canvas.data.pxcorL<=platform[3]and canvas.data.pxcorL-canvas.data.speedH>=platform[3]))and
           (((canvas.data.pycorU>platform[0]and canvas.data.pycorU<platform[1])or
            (canvas.data.pycorD>platform[0]and canvas.data.pycorD<platform[1]))or
           ((canvas.data.pycorD+canvas.data.pycorU)/2>platform[0]and 
            (canvas.data.pycorD+canvas.data.pycorU)/2<platform[1]))):
            if(canvas.data.pxcorR>=platform[2]and canvas.data.pxcorL<=platform[2]):
                canvas.data.pxcorR=platform[2]
                canvas.data.pxcorL=platform[2]-30
            else:
                canvas.data.pxcorL=platform[3]
                canvas.data.pxcorR=platform[3]+30
            isTouching=True
    return isTouching


def keyPressed(event):
    if(event.char=='p'):   
        if(canvas.data.pause==True):
            canvas.data.pause=False
        else:
            canvas.data.pause=True
    if(canvas.data.pause==False):
        if(canvas.data.isTitle==True):
            if(event.char==' '):
                canvas.data.isTitle=False
        else:
            if(event.keysym=='Left'):
                canvas.data.facing="left"
                canvas.data.speedH=-6
            elif(event.keysym=='Right'):
                canvas.data.facing="right"
                canvas.data.speedH=6
            if(event.keysym=='Up' and canvas.data.jumping==False):
                canvas.data.jumping=True
                canvas.data.speedV=12 
                canvas.data.pycorU-=1
                canvas.data.pycorD-=1
        '''if(event.keysym=='Left'):
        elif(event.keysym=='Right'):
        elif(event.keysym=='Down'):
        elif(event.keysym=='Up'):
        elif(event.char==' '):
        elif(event.char=='r'):   
            init()'''
    
def keyReleased(event):
    if(canvas.data.pause==False):
        if(canvas.data.isTitle!=True):
            if(event.keysym=='Left'):
                canvas.data.speedH=0
            elif(event.keysym=='Right'):
                canvas.data.speedH=0

run()

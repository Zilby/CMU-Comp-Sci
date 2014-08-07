#Final Project!!!!!

from Tkinter import *
import random

def run():
    root=Tk()
    global canvas
    canvas=Canvas(root,width=600,height=600,bg='#%02x%02x%02x' % (35, 0, 61)) #for rgb value
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
    canvas.data.nextLevel=True #used for both getting to next level and restarting level
    canvas.data.alive=True
    canvas.data.lives=10
    canvas.data.pxcorL=0 #player xcor left
    canvas.data.pxcorR=0 #player xcor right
    canvas.data.pycorU=0 #player ycor up
    canvas.data.pycorD=0 #player ycor down
    canvas.data.facing="right" #player direction
    canvas.data.jumping=False #aka: isInAir?
    canvas.data.attacking=False 
    canvas.data.attackTimer=0 #used so that can't attack constantly
    canvas.data.speedH=0 #horizontal speed
    canvas.data.speedV=0 #vertical speed
    canvas.data.animationTimer=3 #timer for walking animation
    canvas.data.still=True #whether or not player is moving
    canvas.data.platformTimer=0 #used for deleting platforms 
    canvas.data.firstPlatform=True #used to determine if first platform is still there (special case)
    canvas.data.platforms=[] #array of platforms
    canvas.data.enemy1s=[] #array of enemy1s
    canvas.data.enemy2s=[] #array of enemy2s
    canvas.data.projectiles=[] #array of player projectiles
    canvas.data.projectileRs=[] #array of enemy projectiles
    canvas.data.attackL=PhotoImage(file="attackL.gif")  #image files
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
    canvas.data.Backdrop=PhotoImage(file="backdropC.gif")

def timerFired():
    if(canvas.data.isGameOver==False and 
       canvas.data.pause==False and 
       canvas.data.isTitle==False):
        redrawAll() #general draw everything function
        movePlayer() #moves player
        if(touchingGround()==False): #if not touching anything, fall
                canvas.data.jumping=True
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
    canvas.create_image(0,0,anchor=NW,image=canvas.data.Backdrop)
    if(canvas.data.firstPlatform==True):
        canvas.create_rectangle(0,540,600,600,fill='#%02x%02x%02x' % (44,44,44)) #special color for first ground
    else:
        canvas.create_rectangle(0,540,600,600,fill="black") #special color to show lives, score and level
    canvas.create_text(20, 560, anchor=NW, font="Fixedsys",text="Score: "+str(canvas.data.score),fill="white")
    canvas.create_text(150, 560, anchor=NW, font="Fixedsys",text="Lives: "+str(canvas.data.lives),fill="red")
    canvas.create_text(510, 560, anchor=NW, font="Fixedsys",text="Level: "+str(canvas.data.level),fill="blue")
    drawLevel(canvas.data.level)

def drawLevel(level):
    if(canvas.data.firstPlatform==True):
        for platform in canvas.data.platforms[1:]: #only draws everything but first platform if it's still there
            canvas.create_rectangle(platform[2],platform[0],platform[3],platform[1],fill='#%02x%02x%02x' % (27+(platform[4]*3/5),0,40+platform[4]))#28
    else:
        for platform in canvas.data.platforms: #otherwise draws everything
            canvas.create_rectangle(platform[2],platform[0],platform[3],platform[1],fill='#%02x%02x%02x' % (27+(platform[4]*3/5),0,40+platform[4]))
    for orb in canvas.data.projectiles:
        canvas.create_image(orb[0],orb[2],anchor=SW,image=orb[4])
        if(orb[5]>0):
            moveOrb(orb) #ie: if orb timer has not run out move orb
        else:
            canvas.data.projectiles.remove(orb) #otherwise delete it
    for enemy in canvas.data.enemy1s:
        alive=True
        moveEnemy(enemy)
        for orb in canvas.data.projectiles:
            if(enemyTouching(enemy,orb)==True):
                canvas.data.enemy1s.remove(enemy)
                canvas.data.projectiles.remove(orb)
                canvas.data.score+=10
                alive=False
        if(enemyTouchingP(enemy)==True):
            level=loseLife(level)
        elif(alive==True):
            eImage=None
            if(enemy[4]=="right"):
                eImage=canvas.data.Enemy1R
            else:
                eImage=canvas.data.Enemy1L
            canvas.create_image(enemy[0],enemy[1],anchor=SW,image=eImage)
    if(canvas.data.pycorD<0): #if at top, level complete
        canvas.data.nextLevel=True
        canvas.data.score+=canvas.data.level*100
    if(canvas.data.pycorU>600):  #if at bottom, you lose a life
        level=loseLife(level)
    if(level==0):
        if(canvas.data.nextLevel==True): #resets variables for level 0, sets up level 1
            canvas.data.level=level+1
            canvas.data.nextLevel=False
            canvas.data.facing="right"
            canvas.data.attacking=False
            canvas.data.jumping=False
            canvas.data.speedV=0
            canvas.data.speedH=0
            canvas.data.projectiles=[]
            canvas.data.still=True
            canvas.data.pxcorL=50
            canvas.data.pxcorR=canvas.data.pxcorL+30
            canvas.data.pycorD=540
            canvas.data.pycorU=canvas.data.pycorD-40
            canvas.data.platforms=[[540,600,0,600,random.randint(0,80)],[470,540,300,420,random.randint(0,80)], #[ycorD,ycorU,xcorL,xcorR,color]
                                   [430,450,500,600,random.randint(0,80)],[380,400,250,400,random.randint(0,80)],
                                   [430,450,100,200,random.randint(0,80)],[360,380,0,80,random.randint(0,80)],
                                   [290,310,100,180,random.randint(0,80)],[220,240,0,80,random.randint(0,80)],
                                   [150,170,100,180,random.randint(0,80)],[90,110,200,330,random.randint(0,80)],
                                   [90,110,400,500,random.randint(0,80)],[30,50,520,600,random.randint(0,80)]]
            canvas.data.platformTimer=100
            canvas.data.firstPlatform=True
    else:
        if(canvas.data.nextLevel==True): #generic variable reset for all levels
            canvas.data.level=level+1
            canvas.data.nextLevel=False
            canvas.data.attacking=False
            canvas.data.jumping=False
            canvas.data.still=True
            canvas.data.speedV=0
            canvas.data.speedH=0
            canvas.data.projectiles=[]
            canvas.data.projectileRs=[]
            canvas.data.platforms=[]
            canvas.data.enemy1s=[]
            canvas.data.enemy2s=[]
            canvas.data.firstPlatform=True
            if(canvas.data.level==2): #specific setup for level 2
                canvas.data.facing="left"
                canvas.data.pxcorL=520
                canvas.data.pxcorR=canvas.data.pxcorL+30
                canvas.data.pycorD=540
                canvas.data.pycorU=canvas.data.pycorD-40
                canvas.data.platformTimer=80
                canvas.data.platforms=[[540,600,0,600,random.randint(0,80)],[480,500,150,450,random.randint(0,80)],
                                       [410,430,0,110,random.randint(0,80)],[340,360,100,180,random.randint(0,80)],
                                       [270,290,0,80,random.randint(0,80)],[210,230,150,430,random.randint(0,80)],
                                       [150,170,480,600,random.randint(0,80)],[80,100,120,410,random.randint(0,80)],
                                       [40,60,0,60,random.randint(0,80)]]
                canvas.data.enemy1s=[[300,480,200,400,"right",4],[300,210,200,400,"left",8],[300,80,120,410,"right",10]] #[xcorL,ycorD,start,end,direction,speed]
        else: #if not setting up, set the player image to the correct one
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
            canvas.create_image(canvas.data.pxcorL-5,canvas.data.pycorD,anchor=SW,image=playerImage) #draw the player
            removePlatforms(canvas.data.level,len(canvas.data.platforms)) #remove any platforms that need removing from screen

def drawTitle():
    canvas.delete(ALL)
    canvas.create_image(0,0,anchor=NW,image=canvas.data.Title)

def loseLife(level):
    canvas.data.lives-=1
    if(canvas.data.lives<1):
        canvas.data.isGameOver=True
    else:
        level-=1
        canvas.data.score-=50
        canvas.data.nextLevel=True
    return level

def drawGameOver():
    canvas.delete(ALL)
    canvas.create_rectangle(20,20,580,580,fill="black",width=0)
    canvas.create_text(300,250,font="Fixedsys",text="Game Over",fill="red")
    canvas.create_text(300,300,font="Fixedsys",text="Score: "+str(canvas.data.score),fill="blue")
    canvas.create_text(300,350,font="Fixedsys",text="Press R to Restart",fill="red")

def movePlayer():
    if(canvas.data.speedH!=0 and canvas.data.attacking==False): #if not still or attacking
        if(touchingPWall()==False): #and not touching a platform wall
            if((canvas.data.speedH>0 and canvas.data.pxcorR>=598)!=True and #and not past the screen
               (canvas.data.speedH<0 and canvas.data.pxcorL<=2)!=True):
                canvas.data.pxcorL+=canvas.data.speedH #add the horizontal speed to coordinates
                canvas.data.pxcorR+=canvas.data.speedH
                if(canvas.data.jumping==False):
                    if(touchingGround()==False):
                        canvas.data.jumping=True
                    else:
                        if(canvas.data.animationTimer==0): #switches still and walking images to make animation
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
    elif(canvas.data.attacking==True): #if attacking is true, attack
        attack()
    else:
        if(canvas.data.jumping==False): #if no horizontal or vertical movement, player is still
            canvas.data.still=True
    if(canvas.data.jumping==True): #if in the air and not touching ground
        if(touchingGround()==False):
            for platform in canvas.data.platforms:
                if(canvas.data.pycorU<=platform[1]and #if hits head on platform
                   canvas.data.pycorU>=platform[0]and
                   canvas.data.pxcorR>platform[2]and 
                   canvas.data.pxcorL<platform[3]and 
                   canvas.data.speedV>0):
                    canvas.data.speedV=0 #vertical speed goes to 0
            canvas.data.pycorD-=canvas.data.speedV
            canvas.data.pycorU-=canvas.data.speedV
            canvas.data.speedV-=1
            touchingGround()
        else:
            canvas.data.jumping=False #if it lands, jumping is false, vertical speed is 0
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

def enemyTouchingP(enemy): #enemy touching player
    isTouching=False
    if((((canvas.data.pxcorR-10>=enemy[0]and (canvas.data.pxcorR-10)-canvas.data.speedH<=enemy[0]-enemy[5])or
         (canvas.data.pxcorL+10<=enemy[0]+30 and (canvas.data.pxcorL+10)-canvas.data.speedH>=enemy[0]+30-enemy[5]))or 
        ((canvas.data.pxcorL+canvas.data.pxcorR)/2>enemy[0]and
         (canvas.data.pxcorL+canvas.data.pxcorR)/2<enemy[0]+30))and
       (((canvas.data.pycorU>enemy[1]-30 and canvas.data.pycorU<enemy[1])or
         (canvas.data.pycorD>enemy[1]-30 and canvas.data.pycorD<enemy[1]))or
        ((canvas.data.pycorD+canvas.data.pycorU)/2<enemy[1]and 
         (canvas.data.pycorD+canvas.data.pycorU)/2>enemy[1]-30))):
        isTouching=True
    return isTouching

def touchingPWallX(x): #touching platform wall for variant X
    isTouching=False
    for platform in canvas.data.platforms:
        if(((x[1]>=platform[2]and x[1]-x[6]<=platform[2])or
           (x[0]+10<=platform[3]and (x[0]+10)-x[6]>=platform[3]))and
           (((x[3]>platform[0]and x[3]<platform[1])or
            (x[2]>platform[0]and x[2]<platform[1]))or
            ((x[2]+x[3])/2>platform[0]and 
             (x[2]+x[3])/2<platform[1]))):
            if(x[1]>=platform[2]and x[0]<=platform[2]):
                x[1]=platform[2]
                x[0]=platform[2]-30
            else:
                x[0]=platform[3]
                x[1]=platform[3]+30
            isTouching=True
    return isTouching

def enemyTouching(enemy,x): #enemy touching variant x (projectile)
    isTouching=False
    if(((x[1]-20>=enemy[0]and (x[1]-20)-x[6]<=enemy[0]-enemy[5])or
        (x[0]+20<=enemy[0]+30 and (x[0]+20)-x[6]>=enemy[0]+30-enemy[5]))and
       (((x[3]>enemy[1]and x[3]<enemy[1]-30)or
         (x[2]>enemy[1]and x[2]<enemy[1]-30))or
        ((x[2]+x[3])/2<enemy[1]and 
         (x[2]+x[3])/2>enemy[1]-30))):
        isTouching=True
    return isTouching

def enemyOnPlatform(enemy,platform):
    if(enemy[1]==platform[0] and
       enemy[2]>=platform[2] and
       enemy[3]<=platform[3]):
        return True
    else:
        return False

def attack():
    if(canvas.data.attackTimer==10):
        start=0
        pImage=0
        if(canvas.data.facing=="right"):
            start=20
            speed=8
            pImage=canvas.data.projectileR
        else:
            start=-20
            speed=-8
            pImage=canvas.data.projectileL
        canvas.data.projectiles+=[[canvas.data.pxcorL+start,canvas.data.pxcorR+start,canvas.data.pycorD+3,canvas.data.pycorU+3,pImage,20,speed]] #xL,xR,yD,yU,image,life,speed
        canvas.data.attackTimer-=1
    elif(canvas.data.attackTimer>0):
        canvas.data.attackTimer-=1
    else:
        canvas.data.attacking=False

def moveOrb(orb):
    if(orb[4]==canvas.data.projectileR):
        orb[0]+=8
        orb[1]+=8
        orb[5]-=1
    else:
        orb[0]-=8
        orb[1]-=8
        orb[5]-=1
    if(touchingPWallX(orb)==True):
        canvas.data.projectiles.remove(orb)

def moveEnemy(enemy):
    if(enemy[0]+30>=enemy[3]):
        enemy[4]="left"
    elif(enemy[0]<=enemy[2]):
        enemy[4]="right"
    if(enemy[4]=="left"):
        enemy[5]=-8
    else:
        enemy[5]=8
    enemy[0]+=enemy[5]

def removePlatforms(level,number):
    if(canvas.data.platformTimer==0):
        if(number>1):
            canvas.data.platforms=canvas.data.platforms[1:]
        else:
            canvas.data.platforms=[]
        alive=False
        for enemy in canvas.data.enemy1s:
            for platform in canvas.data.platforms:
                if(enemyOnPlatform(enemy,platform)==True):
                   alive=True
            if(alive!=True):
                canvas.data.enemy1s.remove(enemy)
            else:
                alive=False
        if(level==1):
            if(number==12 or number==11 or number==10):
                if(number==12):
                    canvas.data.firstPlatform=False
                canvas.data.platformTimer=50
            elif(number<10 and number>5):
                canvas.data.platformTimer=30
            else:
                canvas.data.platformTimer=15
        if(level==2):
            if(number==9):
                canvas.data.firstPlatform=False
                canvas.data.platformTimer=100
            elif(number==5 or number==7):
                canvas.data.platformTimer=80
            else:
                canvas.data.platformTimer=30
    else:
        canvas.data.platformTimer-=1
        

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
            if(event.char==' '):
                if(canvas.data.attacking!=True and canvas.data.jumping==False):
                    canvas.data.attacking=True
                    canvas.data.attackTimer=10
            if(event.char=='r'):   
                init()
            if(event.char=='s'):
                canvas.data.nextLevel=True
    
def keyReleased(event):
    if(canvas.data.pause==False):
        if(canvas.data.isTitle!=True):
            if(event.keysym=='Left'):
                canvas.data.speedH=0
            elif(event.keysym=='Right'):
                canvas.data.speedH=0

run()

from Tkinter import *

def mousePressed(event):
    canvas.data.kesdens += [(event.x, event.y)]
    redrawAll()

def keyPressed(event):
    if event.char == 'd':
        if len(canvas.data.kesdens) != 0:
            canvas.data.kesdens.pop()
    redrawAll()

def timerFired():
    if (len(canvas.data.kesdens) == 0):
        canvas.data.flag = True
    else:
        canvas.data.flag = False
    redrawAll()
    delay = 250 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def redrawAll():
    canvas.delete(ALL)
    for location in canvas.data.kesdens:
        (x, y) = location
        canvas.create_image(x, y, anchor = CENTER, image = canvas.data.kesden_face)
    if canvas.data.flag:
        canvas.create_text(150,60,text="NO MORE KESDENS TO DELETE!", anchor = NW, font = "Purisa 24")

def init():
    canvas.data.kesdens = []
    canvas.data.kesden_face = PhotoImage(file = "kesden.gif")
    canvas.data.flag = True

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width = 1000, height = 900)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()

def generateMultiples(number, start):
    if(start%number!=0):
        print "start is not a multiple of given number"
    x=start
    while True:
        yield x
        x+=number

GM=generateMultiples(3,27)
y=True
while(y):
    z=GM.next()
    if(z==81):
        y=False
    else:
        print z

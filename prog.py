#!/usr/bin/python2.7
#chmod +x ./program.py

def helloWorld():
        print "hello world"
        x=5
        y=9
        z=x+y
        print z
        print "Enter your name: ",
        name=raw_input()
        while(z>0):
                print "Hello "+name+", wassup? ("+str(z)+" runs left)"
                z-=1
        i=len(name)
        for s in name:
                i-=1
                if i != 0:
                        print s,
                else:
                        print s
        for i in range(10,20):
                print z
                z+=1

def driver():
        helloWorld()

driver()

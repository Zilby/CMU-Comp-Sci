#!/usr/bin/python2.7
#Lab 1, le python tutorial para los estudiantes de kesden

def One():
    print raw_input("Enter your name: ")

def Two():
    x=int(raw_input("Enter a number: "))
    y=int(raw_input("Enter another number: "))
    print "Your numbers:", x, y

def Three():
    z=1
    while(z<=10):
        if(z!=10):
            print z,
        else:
            print z
        z+=1

def Four():
    x=float(raw_input("Enter floating point number: "))
    y=float(raw_input("Enter another floating point number: "))
    print "Greatest number is",
    if(abs(x)>abs(y)):
        print x
    elif(abs(x)<abs(y)):
        print y
    else:
        print "a tie."

def Five():
    x=int(raw_input("Enter a number: "))
    y=int(raw_input("Enter another number: "))
    print "This question 'compute the average of all numbers between \nthese two numbers, inclusive' could be interpreted in many ways."
    print "\n1) Here is the average of all the numbers between these \ntwo numbers inclusive calculated as quickly as possible:",
    print (x+y)/2
    print "\n2) Here is the average of all the numbers calculated \nusing a loop:",
    if(x>y):
        a=x
        b=y
    else:
        a=y
        b=x
    z=0
    counter=0
    while(b<=a):
        z+=b
        counter+=1
        b+=1
    print z/counter
    print "\n3) And here is the average of every number with every \nother number within the given bounds:"
    if(x>y):
        z=x
        x=y
        y=z
    while(x<y):
        z=x+1
        while(z<=y):
            print "Average of "+str(x)+" & "+str(z)+": "+str((x+z)/2)
            z+=1
        x+=1
    

def Six():
    x=1
    y=1
    while(y<=10):
        while(x<=10):
            if(x*y<10):
                z=str(x*y)+" "
            else:
                z=x*y
            if(x!=10):
                print z,
            else:
                print z
            x+=1
        y+=1
        x=1
    
def Driver():
    print "#1:"
    One()
    print "\n#2:"
    Two()
    print "\n#3:"
    Three()
    print "\n#4:"
    Four()
    print "\n#5:"
    Five()
    print "\n#6:"
    Six()

Driver()

#Part 1:

class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def nonNegative(function):
    def checker(*args):
        try:
            for intList in args:
                for integer in intList:
                    if (integer<0):
                        raise NegativeNumberError("There is a negative")
            return function(*args)
        except NegativeNumberError: 
            return "There is a negative"
    return checker

#arbitrary function
def add(l):
    i=0
    for each in l:
        i+=each
    return i

l1=[9349,592,495,23459,2349,5239,549,349]
l2=[9349,592,495,-23459,2349,5239,549,349]

d1=nonNegative(add)
d2=nonNegative(add)

print d1(l1)
print d2(l2)

#Part 2:

def capitalize(function):
    def caps(*args):
        l=[]
        for sList in args:
            print sList
            for each in sList:
                l.append(each.upper())
        return function(l)
    return caps

#arbitrary function
def addString(l):
    s=""
    for each in l: 
        s+=each+" "
    return s

s=["apple","potato","sAlsa","info","string","yeezus","pika","FTW","Aqua","Uranium","weB","Plebes"]

d3=capitalize(addString)

print d3(s)


#Lab 2

#1
def areComplementary(strand1, strand2):
    try:
        x=0
        s="AGCT"
        while(x<len(strand1)):
            if(strand1[x] not in s or strand2[x] not in s or
               (strand1[x]=='A'and strand2[x]!='T')or
               (strand1[x]=='T'and strand2[x]!='A')or
               (strand1[x]=='G'and strand2[x]!='C')or
               (strand1[x]=='C'and strand2[x]!='G')):
                return False
            x+=1
        if(len(strand1)==len(strand2)):
            return True
        else:
            return False
    except:
        return False

#2
def targetAtIndex(strand, target, i):
    if(i<0 or len(strand)<i+len(target)):
        return False
    x=0
    while(x<len(target)):
        if(strand[i]!=target[x]
           and target[x]!='.'
           and (target[x]!='x'or(strand[i]!='A'and strand[i]!='T'))
           and (target[x]!='y'or(strand[i]!='G'and strand[i]!='C'))
        ):
            return False
        x+=1
        i+=1
    return True

#3
def findTarget(strand, target):
    x=0
    while(x<len(strand)):
        if(targetAtIndex(strand,target,x)):
            return x
        x+=1
    return -1

#def Driver():
#    print areComplementary(raw_input("Enter strand 1: "),raw_input("Enter strand 2: "))
#    print targetAtIndex(raw_input("Enter strand: "),raw_input("Enter target: "),int(raw_input("Enter target index: ")))
#    print findTarget(raw_input("Enter strand: "),raw_input("Enter target: "))

#Driver()

def testAreComplementary():
    print "Testing areComplementary..."
    #assert(areComplementary("A", "T") == True)
    assert(areComplementary("CTAGG", "GATCC") == True)
    assert(areComplementary("CTA", "GATT") == False)
    assert(areComplementary("CTACGC", "GAT") == False)
    assert(areComplementary("GGcT", "CCGA") == False)
    print "All tests passed!"

def testAtIndex():
    print "Testing targetAtIndex..."
    assert(targetAtIndex("A","A",0) == True)
    assert(targetAtIndex("AAAT","AT",2) == True)
    assert(targetAtIndex("AAAT","xT",2) == True)
    assert(targetAtIndex("GCCATA","yA.",2) == True)
    assert(targetAtIndex("GCCATA","TAC",4) == False)
    print "All tests passed!"

def testFindTarget():
    print "Testing findTarget..."
    assert(findTarget("A", "A") == 0)
    assert(findTarget("ATCGGA", "GAT") == -1)
    assert(findTarget("ATACGTG","ACGT") == 2)
    assert(findTarget("TTAGTTA","xyT.") == 2)
    print "All tests passed!"

testAreComplementary()
testAtIndex()
testFindTarget()

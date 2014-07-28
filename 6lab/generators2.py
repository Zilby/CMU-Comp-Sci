
def wordsFromFile(fileName):
    inputfile=open(fileName)
    lines=inputfile.readlines()
    inputfile.close()
    x=[]
    for line in lines:
        x+=line.split()
    while (len(x)!=0):
        yield x[0]
        x=x[1:]

def noPunctuation(wordGenerator):
    output = (word.replace(",","") for word in wordGenerator)
    output = (word.replace(".","") for word in output)
    output = (word.replace(":","") for word in output)
    output = (word.replace(";","") for word in output)
    output = (word.replace("-","") for word in output)
    for word in output:
        yield word

def allCaps(wordGenerator):
    output = (word.upper() for word in wordGenerator)
    for word in output:
        yield word

WFF=wordsFromFile("exfile.txt")

'''
for word in WFF:
    print word
'''

NP=noPunctuation(WFF)

'''
for word in NP:
    print word
'''

AC=allCaps(NP)


'''
I don't know why we had to add to a set
we could have just said
for word in AC:
     print word
but okay then. 
'''

s=([])

for word in AC:
    s.append(word)

for word in s:
    print word

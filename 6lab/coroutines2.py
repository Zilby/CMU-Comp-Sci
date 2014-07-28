inputfile=open("exfile.txt")
line=inputfile.readline()
inputfile.close()

fileWords=(word for word in line.split())

def noPunctuation():
    while True:
        word=yield
        word=word.replace(",","")
        word=word.replace(".","")
        word=word.replace(":","")
        word=word.replace(";","")
        word=word.replace("-","")
        print word

def caps(targetCR):
    while True:
        word=yield
        targetCR.send(word.upper())

NP=noPunctuation()
NP.next()
C=caps(NP)
C.next()

for word in fileWords:
    C.send(word)

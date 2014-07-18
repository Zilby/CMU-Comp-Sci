#Lab 4 para la clase de Sr.Kesden
#because foo bar is clearly spanish

#Part 1:
def readBook(s):
    return tuple(s.split(","))
    
#Part 2: 
def readBooks(s):
    l=[]
    input_file=open(s)
    lines=input_file.readlines()
    for line in lines:
        l.append(readBook(line.strip("\n")))
    return l

#Part 3:
d={}
def buildIndex(l):
    global d
    d={}
    for book in l:
        tList=book[2].split() #List of words in title
        for word in tList:
            if(word.upper()!="AN"and word.upper()!="A"and word.upper()!="THE"):
                d[word]=book[2]
    return d

#Part 4:
def lookupKeyword(d,s):
    output=""
    for word in s.split():
        if(word in d.keys()):
            os=output.split(", ")
            if(d[word] in os):
                output=d[word]+", "
                os.remove(d[word])
                for title in os:
                    output+=title+", "
            else:
                output+=d[word]+", "
    output=output.lstrip().rstrip(", ")
    if(output==""):
        raise NoResultsError("No Books Found")
    else:
        return output

#Part 5:
def presentMenuAndGetChoice():
    r=raw_input("If you wish to initialize an index, enter a .txt file name to initialize\n"
                "or type \"Books, \" followed by a list of titles separated by commas.\n"+
                "If you wish to query an index and receive titles, please enter keywords.\n"+
                "If you wish to quit, please enter ~\n")
    if(r=="~"):
        return 
    rsplit = r.split(", ")
    if(rsplit[0]=="Books"):
        global d
        d={}
        for title in rsplit:
            tList=title.split()
            for word in tList:
                if(word.upper()!="AN"and word.upper()!="A"and word.upper()!="THE"):
                    d[word]=title
        return d
    if ".txt" in r:
        return buildIndex(readBooks(r))
    global d
    try:
        print lookupKeyword(d,r)
    except NoResultsError:
        print "No Book Titles Found"

#Part 6:
class NoResultsError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

#Test Cases:

#print readBook("Zilbersher,Alex,Great Gatsby,12/23/1996,1928372819253")
#print readBooks("4lab.txt")
#Print buildIndex(readBooks("4lab.txt"))
#print buildIndex(readBooks("4lab.txt"))["Affluence"]
#print lookupKeyword(d,"Great")
presentMenuAndGetChoice()
presentMenuAndGetChoice()

#lab 3 for Mr.Kesden 7/14/14

#PART 1:

def factor(n):
    dividend=n
    possibleFactor=2
    factors=[]
    while(dividend!=1):
        if(dividend%possibleFactor==0):
            factors.append(possibleFactor)
            dividend=dividend/possibleFactor
        else:
            possibleFactor+=1
    return factors

print factor(60)
#=> [2, 2, 3, 5]
print factor(45)
#=> [3, 3, 5]
print factor(35)
#=> [5, 7]
print factor(13)
#=> [13]

#PART 2:

def triangle(height):
    i=1
    while(i<=height):
        x=height-i
        y=(2*i)-1
        s=""
        while(x>0):
            s+=" "
            x-=1
        while(y>0):
            s+="*"
            y-=1
        print s
        i+=1

triangle(3)
'''
  *
 ***
*****
'''
triangle(5)
'''
    *
   ***
  *****
 *******
*********
'''

#PART 3:

def doubling(rate):
    low=0.0
    high=10000.0
    guess=5000.0
    guess_error=5000.0
    p=1.0
    while(guess_error>0.001):
        if((p*((1+rate)**guess))-(2*p)>=0):
            high=guess
        else:
            low=guess
        guess=(high+low)/2
        guess_error=(high-low)/2
    return guess

print doubling(0.1)
#=> 7.272540897341713
print doubling(0.05)
#=> 14.206699082890463
print doubling(0.01)
#=> 69.66071689357483

#PART 4:

def factorial(n):
    x = 1
    for i in range(1,n+1):
        x = x * i
    return x

print factorial(4)
#=> 24
print factorial(0)
#=> 1

#PART 5:

def pascal(n):
    for i in range(0,n):
        s=""
        for j in range(0,i+1):
            val=factorial(i)/(factorial(j)*factorial(i-j))
            x=val/10
            if(x<10):
                if(x<1):
                    s+="  "
                else:
                    s+=" "
            s+=" "+str(val)
        print s

pascal(10)
'''
   1
   1   1
   1   2   1
   1   3   3   1
   1   4   6   4   1
   1   5  10  10   5   1
   1   6  15  20  15   6   1
   1   7  21  35  35  21   7   1
   1   8  28  56  70  56  28   8   1
   1   9  36  84 126 126  84  36   9   1
'''

#PART 6:

def num_occurrences(list, key):
    count=0
    for x in list:
        if(x==key):
            count+=1
    return count

print num_occurrences(["a", "b", "a", "b", "c", "b", "d", "e"], "b")
#=> 3

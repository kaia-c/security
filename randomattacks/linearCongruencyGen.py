import math
from random import randint


def listToInt(lst):
    tmp=""
    for num in lst:
        tmp += str(num)
    return int(tmp)



def linConGen(a,b,p,i,crypt):
    global Iters
    if i>1:
        for j, k in zip(a, b):
            crypt.append((a[len(a)-1-i%len(a)]* int(linConGen(a,b,p,i-1,crypt)) + b[len(b)-1-i%len(b)]) % p)
            return listToInt(crypt)
    else:
        return listToInt(crypt)


def convertStr(str1, func):
    str2=[]
    for i in str1:
        str2.append(func(i))
    return str2


def primes():
    primes=[]
    for i in range (1, int(round(8**4))):
        for j in range (2, int(math.sqrt(i))+1):
            if i % j  != 0:
                if j >= int(math.sqrt(i)):
                    primes.append(i)
            else:
                break
    return primes

def checkAsciiRange(num):
    return ((num > 96 and num < 123) or (num > 62 and num < 91) or (num > 43 and num < 58 and num != 47) or num == 242) 

def numToAsciiStr(num):
    numStr=str(num)
    numStr=numStr[1:]
    asciiVals=[]
    for i in range(0, len(numStr)-1):
        tmp=i
        if i<len(numStr)-1 and checkAsciiRange(i+(int(numStr[i+1])*10)):
            tmp+=(int(numStr[i+1])*10)
            numStr=numStr[:(i+1)] + numStr[(i+2):]
            asciiVals.append(tmp)
            i+=1
        elif i<len(numStr)-2 and checkAsciiRange(i + (int(numStr[i+1])*10) + (int(numStr[i+2])*100)):
            tmp += (int(numStr[i+1])*10)
            tmp += (int(numStr[i+2])*100)
            numStr=numStr[:(i+1)] + numStr[(i+3):]
            asciiVals.append(tmp)
            i+=2
    chars=""
    for i in asciiVals:
        chars+=chr(i)
    chars=chars[:32]
    return chars

def intro():
    print("Welcome to the Linear Congruential Generator. \nYou will enter a username and password and receive a 32 charachter crypt.")          

def getInput():
    print("Please use between 6-30 (inclusive) charachters in each of the next entries.  \nYou can use Upper/Lower case letters, numbers, or the symbols @ , _ , . , or -")
    cont = True
    print ("Enter a username:")
    a=convertStr(input(), ord)
    if len(a) < 6 or len(a) > 30:
        cont = False
    else:
        for i in a:
            if not checkAsciiRange(i):
                cont = False
    if cont:
        print ("Enter password:")
        b=convertStr(input(), ord)
        if len(b) < 6 or len(b) > 30:
            cont = False
        else:
            for i in b:
                if not checkAsciiRange(i):
                    cont = False
    return (a, b) if cont else (False, False)


def main():
    intro()
    primeList=primes()
    a=False
    b=False
    while not a or not b:
        a, b = getInput()
        if not a or not b:
            print("\nSorry, there was an error in your input. Please try again.\n")
    p=primeList[randint(0,len(primeList)-1)]
    i=32
    crypt=[1,]
    crypt=linConGen(a,b,p,i,crypt)
    print ("The numeric Crypt is = ", crypt)
    asciiCrypt=numToAsciiStr(crypt)
    print("The asciiCrypt = ", asciiCrypt , " is " , len(asciiCrypt), "chars long.")

main()

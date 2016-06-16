from hashlib import new
from itertools import product
from time import time

startTime=time()
hashToBrute='ed10bac4165a8270ecbdc0cb6a518ad5'
chars=[chr(i) for i in [j for j in range(ord('!'), ord('z'))]]
lenChars=len(chars)
lenGuess=1
try:
    hashFound=False
    while not hashFound:
        tryNum=1
        possiblePermutaions=lenChars**lenGuess
        print("Trying "+ str(lenGuess)+" chars.")
        print("possiblePermutaions="+ str(possiblePermutaions))
        print("Execution time="+str((time()-startTime)/60)+" minutes.")
        for i in product(chars, repeat=lenGuess):
            test=''.join(i)
            if new('md4', test.encode()).hexdigest()== hashToBrute:
                print("A matching string to the hash is: "+test+"\nFound in "+str((time()-startTime)/60)+" minutes.")
                hashFound=True
                break
            tryNum+=1
            if tryNum==possiblePermutaions:
                lenGuess+=1
except KeyboardInterrupt:
    print("Ending operation early, no result")

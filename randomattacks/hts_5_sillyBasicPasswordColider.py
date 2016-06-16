from itertools import product

chars=[chr(i) for i in range(97,108)][::-1]

lenGuess=7
passFound=False
while not passFound:
    for i in product(chars, repeat=lenGuess):
        total=0
        counter=0
        test=''.join(i)
        print(test)
        for j in test:
            total+=(ord(j)+(total*counter))
            counter+=1
        print(total)
        if total > 925559 and total < 927901:
            exit("\n\nPassword: "+test+" scores: " +str(total))

def isPrime(n):
    prime = True
    for i in range(2,int(n//2 +1)):
        if n % i ==0:
            prime = False
            break
    return prime    


givenNumber = 600851475143
primeFactors = []
i=2
while(not isPrime(givenNumber)):
    if(isPrime(i)):
        while(givenNumber % i == 0):
            givenNumber = givenNumber / i
            primeFactors.append(i)
        i+=1
    else:
        i+=1


primeFactors.append(givenNumber)
        
print(max(primeFactors))
            
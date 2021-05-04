def sumOfSquares(n):
    sum = 0
    for i in range(n+1):
        sum += i**2 
    return sum 


def squareOfSum(n):
    return ((n**2 + n)/2) *((n**2 + n)/2)

print(squareOfSum(100)-sumOfSquares(100) )

first = 0
second = 1
sumOfEven = 0
for i in range(4000000-2):
    nextValue = first + second
    if(nextValue > 4000000):
        break
    if  nextValue%2 == 0:
        sumOfEven+=nextValue
    first  = second
    second = nextValue

print(sumOfEven)
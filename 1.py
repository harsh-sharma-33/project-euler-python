def multiplesOf3_5(num) :
    multiples = []
    for i in range(2,num):
        if (i % 3 == 0 or i % 5 ==0 ):
            multiples.append(i)   
    return multiples


print(sum(multiplesOf3_5(1000)))
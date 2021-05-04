def isPalindrome(n):
    n=str(n)
    return  n == n[::-1]


palindrome = []

for i in range(100,1000):
    for j in range(100,1000):
        if ( len(str(i*j))==6 and isPalindrome(i*j)):
            palindrome.append(i*j)
            


print(max(palindrome))
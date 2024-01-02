import random

def getEvenOdd(n):
    print(n)
    if n%2==0:
        return "Even Number"
    else:
        return "Odd Number"

def getVal(n):
    return n,n+1,n+2



n = random.randint(1,100)
ans = getEvenOdd(n)
print(ans)


a,b,c = getVal(5)
print(a)
print(b)
print(c)
def hello():
    print("Hello World")

def greet(name):
    print("Hello "+name)
    
def add(a,b):
    print(a+b)

def fib(N,a=0,b=1):
    i=0
    while i<N:
        c=a
        a=b
        b=c+b
        print(a,end=" ")
        i+=1
    print()

def swap(a,b):
    a,b = b,a
    print("a= "+ str(a))
    print("b= "+str(b))   

hello()

greet("Vishnu")

add(2,5)

fib(10)
fib(10,1,1)

swap(1,2)
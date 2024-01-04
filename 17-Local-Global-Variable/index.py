x = 4
print(f"out the function {x}") #x is not accesseble bcoz it is a global variable

def hello():
    global y  #makes y global variable
    y = 10
    print(f"in the function {x}") #x is not accesseble bcoz it is a global variable
    print(f"in the function {y}")
    
#- y is not defined
print(f"out the function{y}") #y is not accesseble bcoz it is a local variable of hello function 

hello()
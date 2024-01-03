q = ["Who is father of nation?","Who is PM of india?","Who sang Natu Natu in RRR movie?"]
a = ["Gandhi","Narendra Modi","Rahul Sipligunj"]
o = [["a)Gandhi","b)Nehru","c)None"],["a)Vishnu","b)Narendra modi","c)Gandhi"],["a)Lata Mangeshwar","b)Raveena Singh","c)Rahul Spiligunj"]]

i=0
total = 0
while i<len(q):
    print(q[i])
    for x in o[i]:
        print(x,end="  ")
    ans = str(input("Choose an option from a,b,c>"))
    if i==0 and ans == "a":
        total = 100
    elif i==1 and ans == "b":
        total *= 100
    elif i==2 and ans == "c":
        total *= 100
    else:
        break
    i = i+1
print("You Won "+str(total)+" ruppess")
print("Thank you")
    
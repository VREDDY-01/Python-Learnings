l = [3,5,6,"vishnu",True]

print(l)
print(type(l))

# Access data
print(l[0])
print(l[1])
print(l[-1]) #len(l)-1
if 5 in l:
    print("YES")
else:
    print("NO")

# loop
for i in l:
    print(i,end="-")
print()

#slicing
print(l[1:3:2]) #l[start:end:steps]

#List Comprehension
lst = [i for i in range(4)]
print(lst)
lst = [i for i in range(4) if i%2==0]
print(lst)




# WHILE LOOP
num = 0

while num<5:
    print(num)
    num += 1
print("-----------")

# FOR LOOP 
# range([start],(end),steps)
# range(end)
# range([start],(end))
for i in range(5):
    print(i)
print("-----------")
    
for i in range(5,10):
    print(i)
print("-----------")

for i in range(5,11,2):
    print(i)
print("-----------")

for i in range(5,0,-1):
    print(i)
print("-----------")

# break and continue

for n in range(20):
    if n%2==0:
        continue
    elif n==11 or n==15:
        break
    print(n,end=",")
print()
print("-----------")
 
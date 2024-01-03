t = (1,2,6,8,5)
print(t)

temp = list(t)
temp.pop()
temp.append(12)
temp.remove(6)
temp.sort()
# ...all list methods

t = tuple(temp)

print(t)
print(t.count(1))
print(t.index(1,0,4))
print(len(t))
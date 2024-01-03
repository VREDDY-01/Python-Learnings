l = [i for i in range(10)]

print(l)

l.append(4)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

print(l.count(4))

m=l.copy()
m[0]=-1
print(m)
print(l)

k=l+m
print(k)
print(l)

l.extend(m)
print(l)
s1 = {1,2,5,2,6}
s2 = {3,6,8,6,7,3,8,9}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

s1.add(9)
print(s1)

s1.update(s2)
print(s1)

s1.intersection_update(s2)
print(s1)
f = open("1.txt","r")
# "r" -> read mode
# "w" -> write mode
# "a" -> append mode
print(f)

text = f.read()
f.close()

print(text)
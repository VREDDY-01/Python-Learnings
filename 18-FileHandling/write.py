f = open("2.txt","w")
r = open("2.txt","r")
# "r" -> read mode
# "w" -> write mode
# "a" -> append mode

f.write("Hi bro, I am fine! ")
f.write("How are you")
f.close()

txt = r.read()
r.close()
print(txt)

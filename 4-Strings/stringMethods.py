name = "VisHnu Teja"
spaces1 = "teja       "
spaces2 = "teja!!!!!!!"

print(len(name))
print(name.upper())
print(name.lower())
print(spaces1.strip())
print(spaces2.rstrip("!"))
print(spaces2.replace("!","$"))
print(name.split(" "))
print(spaces1.capitalize())
print(name.center(5))
print(name.startswith("V"))
print(name.endswith("ja"))
print(name.endswith("ja",4,8)) #[4,8)
print(name.find("ja"))
print(name.isalnum()) # because of space
print(name.isalpha()) # because of space
print(spaces1.islower())
print(name.isupper())
print(name.isspace())
print(name.swapcase())
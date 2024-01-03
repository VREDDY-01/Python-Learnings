import time

t = int(time.strftime("%H"))


if t>=6 and t<12:
    print("GOOD MORINING")
elif t>=12 and t<18:
    print("GOOD AFTERNOON")
elif t>=18 and t<22:
    print("GOOD EVENING")
else:
    print("GOOD NIGHT")
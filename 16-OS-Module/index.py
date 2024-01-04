import os

# print(dir(os))

# os.mkdir("./data")
for i in range(0,10):
    os.mkdir(f"Day-{i}")

if(not os.path.exists("data")):
    os.mkdir(f"data")
    
os.rename("data","Secrets")

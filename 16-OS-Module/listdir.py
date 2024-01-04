import os
import shutil

if os.path.exists("data"):
    folders = os.listdir("data")


# for folder in folders:
#     print(folder)

if os.path.exists("Secrets"):
    os.rmdir("Secrets")

if os.path.exists("data"):
    shutil.rmtree("data")

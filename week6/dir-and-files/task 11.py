import os

s = str(input("Path: "))

if os.access(s, os.F_OK):
    os.remove(s)
else:
    print("File not found")
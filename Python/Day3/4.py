#!/usr/bin/python3
try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except:
    print("Error")
finally:
    print("blah")


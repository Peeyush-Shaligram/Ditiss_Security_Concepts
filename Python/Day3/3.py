#!/usr/bin/python3
import argparse, subprocess as ss
parser = argparse.ArgumentParser(description = "This is resolve tool")
parser.add_argument("-f", type = str, help="provide command", required=False)
parser.add_argument("-o", type = str, help="provide command", required=False)
a = parser.parse_args()
p = open(a.f, "r")
x= p.readlines()
for i in x:
    if a.o:
        q = open(a.o, "a")
        y = q.writelines(ss.getoutput("host -t a {}".format(i)))
        q.close()
    else:
        print(ss.getoutput("host -t a {}".format(i)))
    
p.close()


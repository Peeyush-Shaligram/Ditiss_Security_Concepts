#!/usr/bin/python3
import requests, argparse 

parser = argparse.ArgumentParser(description="This is a Active Sub domain lister Tool")
parser.add_argument("-f", type=str, help="Provide Command", required=True)

a=parser.parse_args()

p=open(a.f, "r")
x=p.readlines()


#try:
for i in x:
    z = i.strip()
    url = "http://[{}]".format(z)
    h = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
    data = requests.get(url, headers=h, allow_redirects=False)

    c = data.status_code

    if c==200:
        print(url + "{}".format(c))
    elif c==301 or c==302:
        print("https://", str(i.strip()), "[{}]".format(c))
    elif c==403 or c==404:
        print(url, "[{}]".format(c))
p.close()




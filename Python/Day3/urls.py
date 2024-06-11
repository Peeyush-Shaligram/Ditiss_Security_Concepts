#!/usr/bin/python3

import requests,random

url = "https://pastebin.com/raw/01yJu4gY"

h = {'user-Agent':'me_peeyush'}

data = requests.get(url, headers=h, timeout=10)

x = data.text.split("\r\n")


for i in x:
    data2 = requests.get(i)
    num = str(random.randint(1,100))
    f = open("images"+num+".jpg","wb")
    f.write(data2.content)
    f.close()

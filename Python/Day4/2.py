#!/usr/bin/python3
import requests as rr

url = "http://192.168.43.101:83/"
header = '{"User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) "}'

#payload = '{"username":"admin","password":"71urlkufpsdnlkadsf"}'
data = rr.get(url,headers=header)

print(data.status_code)
print(data.text)
#print(data.content)
#print(data.headers.items())

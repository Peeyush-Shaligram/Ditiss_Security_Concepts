#!/usr/bin/python3
import requests
    url = "https://webhook.site/a7d47df1-0153-4449-b8c3-570f300e665e"
    h = {'user-Agent':'Akatsuki'}
    data = requests.get(url, headers=h, allow_redirects=True, timeout=10)

    print(data.status_code)








#print(data.headers)
#print(data.headers['Server'])
#print(data.headers.items())
#for a,b in data.headers.items():
#    print("{}: {}".format(a,b))
#print(data.text)

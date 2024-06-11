#!/url/bin/python3

import requests

url = "https://lhwmis.sindhealth.pk/img/lhwimg2.jpg"
h = {'user-Agent':'me_peeyush'}
data = requests.get(url, headers=h, timeout=10)
print(type(data.text))
print(type(data.content))

f = open("image.jpg", "wb")
f.write(data.content)
f.close()

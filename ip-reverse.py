import requests as ts
from bs4 import BeautifulSoup
from time import sleep as s
#Ch0l0h4twh1t3

web =input("IP o Dominio: ")
payload = {'User-Agent': 'Firefox'}
req = ts.get(f'https://viewdns.info/reverseip/?host={web}&t=1',headers=payload)
r = BeautifulSoup(req.text, 'html5lib')
r1 = r.find(id='null')
read = r1.find(border='1')

try:
    for i in read.find_all('tr'):
        s(0.02)
        print('\033[32mDominio  ->>   '  +"\033[31m",i.td.string)
except AttributeError:
    print("Argumento Invalido!")


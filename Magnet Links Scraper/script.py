from bs4 import BeautifulSoup
import re


f = open("data.html", "r")
data = "".join(f.readlines())
f.close()
arr = []
bs = BeautifulSoup(data, features='lxml')
for link in bs.findAll('a'):
    linkdata = str(link.get('href'))
    if "magnet:" in linkdata:
        arr.append(linkdata+"\n")

f = open('links.txt', 'w')
f.writelines(arr)
f.close

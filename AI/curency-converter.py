import xml.etree.ElementTree as xml
from urllib.request import urlopen
import json.scanner

currency_symbols = dict()

api = urlopen("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml")
tmp = api.read().decode('utf-8')
tree = xml.fromstring(tmp)
for child in tree[2]:
    for c in child:
        currency_symbols[c.attrib['currency']] = c.attrib['rate']
currency_symbols['EUD'] = 1

# print(currency_symbols['EUD'])
# exit(0)
toRateSym = 'USD'
toRate = float(currency_symbols[toRateSym])
fromRateSym = 'INR'
fromRate = float(currency_symbols[fromRateSym])
amount = 100.00
convertedAmount = amount * toRate/fromRate
print(toRate)
print(fromRate)
print(convertedAmount)


import json
from urllib.request import urlopen

# base currency
baseCurrency = 'USD'

# exchange rate url
xchgRateURL = 'https://api.exchangerate-api.com/v4/latest/' + baseCurrency

print (xchgRateURL)

with urlopen(xchgRateURL) as response:
  source = response.read()

data = json.loads(source)
# print (json.dumps(data, indent=2))
# print (data['rates'])

for sym, xRate in data['rates'].items():
  print (f'Symbol: {sym}, Exchange Rate: {xRate} (type: {type(xRate)})')


import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
#print(sopa)
#print(sopa.select('title'))
#print(sopa.select('title')[0].getText())
#print(sopa.select('p'))
#print(len(sopa.select('p')))
parrofo_especial = sopa.select('p')[1].getText()
print(parrofo_especial)


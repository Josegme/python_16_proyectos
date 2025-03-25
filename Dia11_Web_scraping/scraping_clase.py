import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2024/07/por-que-se-utiliza-python-en-ciencia-de.html?m=1')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#parrafo_central = sopa.select('.container p')[2]
parrafo_central = sopa.select('.page p')

for p in parrafo_central:
    print(p.getText())
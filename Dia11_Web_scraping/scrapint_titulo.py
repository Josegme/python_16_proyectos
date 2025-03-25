#para obtener libros con caracteristicas especificas.
#para el caso estrellas

import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

libros = sopa.select('.product_pod')

ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)


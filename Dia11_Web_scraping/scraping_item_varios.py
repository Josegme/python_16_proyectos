import bs4
import requests

# crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de títulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):

    # crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # chequear que tengan 4 o 5 estrella
        if len(libro.select('.sart-rating.Four')) != 4 or len(libro.select('.sart-rating.Four')) != 5:

            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver libros 4 u 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)



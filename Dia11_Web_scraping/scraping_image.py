import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/l/products')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#para encontrar las imagenes que quiero obtener
imagenes = sopa.select('img')

for i in imagenes:
    print(imagenes)

#para que busque solo elemento del indice que quiero
imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso_1 = requests.get(imagenes)
#print(imagen_curso_1_content)
f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()
#Se deberia crear una img dentro de mi carpeta
#Se puede colocar con un loop para descargar todas las img del sitio

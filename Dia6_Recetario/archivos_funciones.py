"""
Crea una función llamada registro_error() que abra (open)
un archivo indicado como parámetro, y lo actualice
añadiendo una línea al final que indique
"se ha registrado un error de ejecución".
Finalmente, debe cerrar el archivo abierto.
"""
def registro_error(archivo_par):
    with open(archivo_par, 'a') as archivo:
        archivo.write('se ha registrado un error de ejecución')

registro_error('Prueba.txt')

with open('Prueba.txt', 'r') as archivo:
    print(archivo.read())


"""
Crea una función llamada sobrescribir() que abra (open)
un archivo indicado como parámetro, y sobrescriba cualquier
contenido anterior por el texto "contenido eliminado"
"""
def sobrescribir(archivo_txt):
    with open(archivo_txt, 'w') as archivo:
        archivo.write('contenido eliminado')

sobrescribir('Prueba.txt')






"""
Crea una función llamada abrir_leer() que abra (open)
un archivo indicado como parámetro,
y devuelva su contenido (read).
"""

def abrir_leer(archivo_txt): #parametro sin comillas
    with open(archivo_txt, 'r', encoding='utf-8') as archivo: #with open para que se cierre el archivo
        return archivo.read()

contenido = abrir_leer('Prueba.txt')
print(contenido) #si existe el archivo en la misma carpeta devuelve para lectura










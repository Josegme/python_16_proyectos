from ej_pathlib import Path
#para mac se utiliza / y se pude abrir en un SO windows
carpeta = Path('C:/Equipo120424M/Desktop/GPI_MKT/1_Full_Stack/Contenido_Python_Total/dia 6/alternativa')
archivo = carpeta / 'Prueba_alternativa.txt'
#siempre con el objeto Path adelante

mi_archivo = open(archivo)
print(mi_archivo.read())

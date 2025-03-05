"""
hay diferentes modos de leer el archivo por
open recibe dos parametros en realidad uno es el archivo.texto
y el otro es el modo en que va a abrir ese archivo
mi_archivo = open('archivo.txt','r')
r es en modo read o solo lectura: por lo tanto solo va a leer el contenido y no va hacer otra accion
w es en modo write o solo escritura: si el archivo ya existe o crea
a es un modo escritura al final del archivo, se puede escribir desde el final

"""

archivos1 = open('prueba1.txt')
archivos1.readline()
segunda_linea = archivos1.readline()
print(segunda_linea)

#print(archivos1.read())
print(archivos1.readline())
archivos1.close()

mi_archivo = open('prueba.txt')
"""
print(mi_archivo.readline())

print(mi_archivo.readline())

print(mi_archivo.readline())
"""
todas = mi_archivo.readlines()
print(todas)
#puedo aplicar los métodos de lista
todas = todas.pop()
print(todas)
#cada vez que carguemos readline se va a cargar todo el archivo
#siempre cerrar para no sobrecargar y ocupar espacio

for linea in mi_archivo:
    print("Aqui dice: "+ linea)

una_linea = mi_archivo.readline()
print(una_linea.upper()) #puedo aplicar los métodos de string

una_linea = mi_archivo.readline()
print(una_linea.rstrip())
#si queremos que se muestres sin el salto de línea
una_linea = mi_archivo.readline()
print(una_linea)


#una_linea = mi_archivo.readline()
#print(una_linea)
"""
print(mi_archivo) #esto solo me da info de la variable
#la variable tiene métodos asociados
print(mi_archivo.read()) #abrimos, leemos y mostramos
 #para guardar espacio de memoria en el ordenador para
# que siempre se cierre al final de la ejecucion
"""
mi_archivo.close()
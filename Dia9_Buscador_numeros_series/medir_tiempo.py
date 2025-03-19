import timeit

declaracion = """
prueba_for(10)
"""
mi_setup = """
def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista
"""

duracion = timeit.timeit(declaracion, mi_setup, number= 100000)
print(duracion)

declaracion2 = """
prueba_while(10)
"""
mi_setup2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""
duracion2 = timeit.timeit(declaracion2, mi_setup2, number=100000)
print(duracion2)

"""
def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista
print(prueba_for(15))
print(prueba_while(15))

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time() #control de timepo antes de ejecutarse
prueba_for(1000000)
final = time.time() #control de tiempo luego de ejecutarse
print(final-inicio)

inicio = time.time()
prueba_while(1000000)
final = time.time()
print(final-inicio)

ESTO SIRVE CUANDOS SON VALORE GRANDES POR ESO UTILIZAMOS TIMEIT
"""



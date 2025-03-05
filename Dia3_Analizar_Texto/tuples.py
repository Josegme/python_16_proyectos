#Ejercicios:
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))
mi_tupla2 = (1, 2, 3, 2, 3, 1, 3, 2)
mi_tupla2 = list(mi_tupla2)
mi_lista = mi_tupla2
print(type(mi_tupla2))
#extraer elementos de la tupla
mi_tupla3 = (1, 2, 3, 4)
a, b, c, d = mi_tupla3
print(a, b, c, d)

"""
mi_tuple = (1, 2, 3, 4, 5)
print(type(mi_tuple))
print(mi_tuple[2])
#tupla dentro de tuplas
tup = (1, 2, (10, 20), 4)
print(tup[2]) #puedo buscar el elemento que esta en determinado indicie
print(tup[2][0]) #y puedo tener tuplas dentro de tuplas y buscar elementos
#podemos hacer casting
mi_tuple = list(mi_tuple)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))
t = (1, 2, 3, 1)
#x, y, z = t
#print(x, y, z)
#puedo hacer esto siempre que haya la misma cantidad de valores y elementos
print(t.count(1))
print(t.index(2))
"""

from collections import Counter
from collections import defaultdict
from collections import deque

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

print("Lista inicial de ciudades:", lista_ciudades)
lista_ciudades.appendleft("Lisboa")

print("Lista después de agregar 'Lisboa' a la izquierada:", lista_ciudades)

lista_ciudades.appendleft('Amsterdam')
print("Lista despues de agregar 'Amsterdam' a la izquierda:", lista_ciudades)


#crear un defaultdict que devuelva "" cuando una clave no exista
mi_diccionario = defaultdict(lambda: "valor no hallado")
#cargamos el diccionario
mi_diccionario['edad'] = 44

print(mi_diccionario['edad'])
print(mi_diccionario['nombre'])




lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)

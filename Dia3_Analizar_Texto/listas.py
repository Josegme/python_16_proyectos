#LISTAS
#ejercicios
from turtledemo.sorting_animate import enable_keys

lista = [44, 'pelota', 1.1, 'China', 'rojo']
print(lista)
#ejercicio2
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append('motocicleta')
print(medios_transporte)
#ejercico3
"""Utiliza el método pop() para quitar el tercer elemento de 
la siguiente lista llamada frutas, y almacénalo en una 
variable llamada eliminado. Utiliza métodos de listas sin
 alterar la línea de código ya suministrada."""
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print("Elemento Eliminado: ", eliminado)
print(frutas)
"""
mi_lista = ["a", "b", "c"]
otra_lista = ['hola', 55, 6.1] #podemos tener lista con diferentes tipos de datos
print(type(mi_lista))
resultado = len(mi_lista) #len para ver la cantidad de elementos
print(resultado)
indice = mi_lista[0]
indice1 = mi_lista[0:2]  #podemos buscar los indices igual que los string
print(indice)
print(indice1)
#podemos concatenar listas
mi_lista2 = ['d', 'e', 'f']
concatena_listas = mi_lista + mi_lista2
print(mi_lista + mi_lista2)
print(concatena_listas)
#podemos alterar elementos en la lista
concatena_listas[0] = "alfa"
print(concatena_listas) #puedo sobre ecribir los elementos
#tambien tenemos metodos
mi_lista2.append('g') #agrego elementos a la lista con append
print(mi_lista2)
#tambien puedo eliminar elementos
mi_lista.pop() #por defecto elimina el último elemento de la fila
print(mi_lista)
mi_lista2.pop(0)
print(mi_lista2)
#otros métodos imporantes con las listas puede ser
#ordenar SORT()
lista_ = ['g', 'e', 'm', 'c', 'a']
print(lista_)
lista_.sort()
print(lista_)
lista_.reverse()
print(lista_)
"""


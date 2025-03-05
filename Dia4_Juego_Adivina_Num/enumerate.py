#anumerate
lista = ['a','b','c']

for item in enumerate(lista):
    print(item)

for indice, item in enumerate(lista):
    print(indice,item)
#se puede trabajar con rangos y otras var
for indice, item in enumerate(range(50,55)):
    print(indice,item)
#podemos utilizar dentro de un loop
mis_tuples = list(enumerate(lista))
print(mis_tuples)

print('ejercicios')
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres) :
    print(f'{nombre} se encuentra en el índice {indice}')

lista= "Python"

for indice in enumerate(lista):
    print(indice)

lista = list(enumerate("Python"))
print(lista)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)


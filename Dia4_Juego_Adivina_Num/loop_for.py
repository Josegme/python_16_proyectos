#Loop FOR
#necesitamos un objeto iterable
lista = ['a', 'b', 'c']

for letra in lista: #imprime cada elemento "letra" dentro de la lista
    numero_letra = lista.index(letra) + 1
    print(f"La letra {numero_letra} es: {letra}")  #imprime el elemento "letra"

mi_lista = ['Pablo','Laura','Fede','Luis','Julia']

for nombre in mi_lista: #combinamos loops con control de flujo
    if nombre.startswith('L'):
        print(nombre)
    else:
        print('El nombre no comienza con L')

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor) #como esta dentro del loop va a imprimir cada vez que itere

print(f'Despues de iterar por el loop, sale e imprime: {mi_valor}') #solo va a imprimir el resultado final despues de ejecutar todas las iteraciones

palabra = 'python es genial'

for letra in palabra:
    print(letra)

#podemos hacer que funcione el bucle directamente declarando la variable como objeto
for letra in 'python':
    print(letra)

for numero in [1,2,3]:
    print(numero)

for letra in ('a','b','c'):
    print(letra)

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
    print(b)
#para iterar en un diccionario
dic = {'clave1':'a',
       'clave2':'b',
       'clave3':'c'
       }
for item in dic.items():
    print(item)

for valores in dic.values():
    print(valores)

#otra forma es por indice o elemento
for a,b in dic.items():
    print(a,b)

print("Ejercicios")
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f'Hola {alumno}.')
#ejercicio2
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
    print(suma_numeros)

print(suma_numeros)

#ejercicio 3
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero%2==0:
        suma_pares = suma_pares + numero
        print(suma_pares)
    else:
        suma_impares = suma_impares + numero
        print(suma_impares)
print(f'la suma de números pares es {suma_pares}')
print(f'la suma de números impares es {suma_impares}')


"""la comprensión de listas es una manera dinámica de construir listas
por ejemplo necesitamos crear una lista a traves de un loop o de que dependa
de alguna otra operacion/evento
"""
palabra = 'Python'

lista = []

for letra in palabra:
    lista.append(letra)
#por cada letra en la variable palabra incorpora a la lista con append a cada letra
print(lista)
#esto se puede hacer mas eficiente
lista2 = [letra for letra in palabra]
print(lista2)
#esto se puede mejorar mas
lista3 = [letra for letra in 'Una sola linea']
print(lista3)
#tambien podemos trabajar con numeros
lista4 = [n for n in range(0,21)]
print(lista4)
lista5 = [n1 for n1 in range(0,100,5)]
print(lista5)
lista6 = [n2 / 2 for n2 in range(0,10)]
print(lista6) #podemos operar el num antes que entre a la lista
lista7 = [n for n in range(0,50) if n*0.5>10]
#incorpora al valor n por cada n que este en el rango de 0 a 50
#Si ese numero n por 0.5 da un resultado mayor a 10
print(lista7)
#si quiero incorporar a else cambia un poco la sintaxis
lista8 = [n if n*0.5>10 else 'no' for n in range(0,50)]
print(lista8)

pies = [10,20,30,40,50]
metros = [p*3.281 for p in pies]
print(metros)
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n%2 == 0]
print(valores_pares)
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [((n-32)*5/9) for n in temperatura_fahrenheit]
print(grados_celsius)

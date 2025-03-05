#rango
for numero in range(5): #el rango es hasta 5 por defoult inicia en 0
    print(numero)

for numero in range(20,31): #inicia en 1 finaliza hasta antes del 5 (1, n-1)
    print(numero)

#para saltear numeros
for numero in range(10,100,5):
    print(numero)

lista = list(range(1,50))
print(lista)
#ejercicios
mi_lista = list(range(2500,2586))
print(mi_lista)
#ejercicio2
mi_lista = list(range(3,301,3))
print(mi_lista)
#ejercicio3
suma_cuadrados = 0

for numero in range(1,16):
    suma_cuadrados += numero**2

print(suma_cuadrados)


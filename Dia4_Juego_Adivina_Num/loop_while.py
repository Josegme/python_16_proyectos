"""monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    #tengo que tener la linea que modifica la condicion
    monedas = monedas - 1
else:
    print("No tengo mas dinero")
#siempre hay que declarar en el while la condicion de corte y
# hay que modificar el elemento que itera

#en el loop while puede ser que no tenga el control total, depende de la dinamica
respuesta = 's'

while respuesta == 's':
    respuesta = input("¿Quieres seguir? (s/n)")
else:
    print("Gracias")

#variable = 'pasadelargoconpass'
#while variable == 'pasadelargoconpass':
    #pass

nombre = input("Tu nombre: ")
#break
for letra in nombre:
    if letra == 'v':
        break
    print(letra)
#continue
for letra in nombre:
    if letra == 't':
        continue
    print(letra)
"""
print("Ejercicios While")

numero = 10

while numero >= 0:
    print(numero)
    numero = numero -1

print('Llegamos a cero')

#ejercicio 2
numero = 50

while numero >= 0:
    if numero%5 == 0:
        print(numero)
    numero = numero - 1

#ejercicio3
lista_numeros = [4,5,8,7,-5,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    else:
        print(numero)

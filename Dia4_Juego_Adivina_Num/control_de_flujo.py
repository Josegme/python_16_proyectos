#control de flujo
#ejercicio 2
edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")
#ejercicio 3
habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif habla_ingles and sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")


print('if es "si sucede tal cosa: ejecuta el cod')
if 10 > 9: #solo ve si es True o False la condicion
    print('Es correcto')

x = True
if x:
    print('Es correcto')
print('que pasa si la condición no se cumple')
if 5==2:
    print('Es correcto')
else:
    print('No es correcto')

mascota = 'conejo'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No se que animal tienes')

print('se pueden anidar condiciones')
edad = 16
calificacion = 8

if edad < 18:
    print('eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')

print('Ejercicios con if, else, elif')

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

if num1>num2:
    print(f"{num1} es mayor que {num2}")
elif num2>num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")




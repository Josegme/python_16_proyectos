def numeros_personas(nombre, *args):
    suma = 0
    for arg in args:
        suma += arg  # Sumar los números
    return f'{nombre}, la suma de tus números es {suma}'

# Llamada a la función
print(numeros_personas('Carlos', 2, 3, 4))  # Salida esperada: "Carlos, la suma de tus números es 9"


"""def numeros_personas(nombre, *args):
    nombre = str(input('Escribe tu nombre: '))
    suma = 0
    for arg in args:
        suma = suma + arg
    return f'{nombre}, la suma de tus números es {suma}'


print(numeros_personas('',5,3,6,5))"""

def suma_absoluto(*args):
    suma = 0
    for arg in args:
        suma = suma + abs(arg)
    return suma

print(suma_absoluto(2,-3,8,-10))

def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma = suma + arg**2
    return suma

print(suma_cuadrados(2,2,3,5,6,8))

print(suma_cuadrados(2,2,2))

def suma1(a,b):
    return a+b

print(suma1(5,6))
#ahora utilizando *args vamos a tener un número indefinido de argumentos
#que va a depender de la cantidad que ingrese el usuario
def suma(*args):
    total = 0
    for arg in args:
        total = total + arg #o total += arg
    return total

print(suma(1,1,2,6,8,9,6))

def funcion_suma(*args):
    return sum(args)

print(funcion_suma(1,5,8,9,6))

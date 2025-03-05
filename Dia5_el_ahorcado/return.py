def multiplicar(numero1, numero2):
    return numero1*numero2

print(multiplicar(5, 10))
#lo que se hace habitulamente es guardar en una variable el resultado
resultado = multiplicar(5,2)
print(resultado)

#tambien podemos definir la función con una variable que devuelva la operacion
def multiplicar_sumar(num1, num2):
    total = num1*num2 + num2
    return total

resultado = multiplicar_sumar(5,5)
print(resultado)

print('Ejercicios')
def potencia(num1, num2):
    total = num1**num2
    return total

resultado = potencia(2,5)
print(resultado)

def usd_a_eur(valor):
    cambio = valor*0.9
    return cambio

dolares = usd_a_eur(10000)
print(dolares)

def invertir_palabra(texto):
    invertir = texto[::-1]
    return invertir

def invertir_palabra_2(texto2):
    invertir2 = "".join(reversed(texto2))
    return invertir2

palabra = invertir_palabra("Python")
print(palabra)

palabra2 = invertir_palabra_2("Python2")
print(palabra2)


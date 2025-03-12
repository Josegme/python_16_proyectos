def pedir_numero():

    while True:
        try:
            numero = int(input("dame un numero: "))
        except:
            print("ese no es un numero")
        else:
            print(f"ingresaste el numero {numero}")
            break

    print("gracias")

pedir_numero()
"""
def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1+n2)
    print('gracias por sumar' + n1)

try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un número")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo.")
#entonces podemos preparar para los tipos de errores previstos.
"""
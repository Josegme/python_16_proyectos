#podemos pasar una funcion como argumento de otra funcion
"""
def una_funcion(funcion):
    return funcion

una_funcion(mayuscula("probando"))

def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

operacion = cambiar_letras('may')
operacion2 = cambiar_letras('min')

operacion('palabra')
operacion2('OTRA PALABRA')

"""
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return otra_funcion


def mayuscula(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula('Fede')
mayuscula_decorada = mayuscula_decorada('Fede')



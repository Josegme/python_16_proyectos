def lista_atributos(**kwargs):
    return kwargs

print(lista_atributos(a=1,b=2,c=3))

def cantidad_atributos(**kwargs):
    return len(kwargs)  # Devolvemos un entero en lugar de una cadena

# Prueba
print(cantidad_atributos(a=1, b=2, c=3, d=4, e=5, f='seis', g='siete'))  # Debería imprimir 7
print(cantidad_atributos(x=10, y=20))  # Debería imprimir 2



def cantidad_atributos(**kwargs):
    return f'La cantidad de parámetros es {len(kwargs)}'

print(cantidad_atributos(a=1,b=2,c=3, f='cuatro',g='cinco'))

"""def suma(**kwargs):
    print(type(kwargs))

suma(x=3, y=5, z=2) #vemos que sale como diccionario
"""
def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3,y=5,z=2))

def prueba(num1, num2, *args, **kwargs):

    print(f'El primer valor es {num1}')
    print(f'El segundo valore es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

prueba(15,50,100,300,300,400, x='uno',y='dos', z='tres')

#tambien puedo desempacar con args y kwargs
#si tengo dos variables
args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(15,50,*args, **kwargs)

def lista_atributos(**kwargs):
    return list(kwargs.values()) #extrae los valores y los convertimos en lista

print(lista_atributos(nombre="Juan",edad=30,ciudad="Madrid"))


def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')

    for nombre_argumento, valor_argumento in kwargs.items():
        print(f'{nombre_argumento}: {valor_argumento}')


describir_persona('Maria', color_ojos = 'azules', color_pelo = 'rubio')
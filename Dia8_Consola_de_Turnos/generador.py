def contador_vidas():
    vidas = 3
    while vidas > 0:
        yield f'Te quedan {vidas} vidas'
        vidas -= 1
    yield 'Game Over'

perder_vidas = contador_vidas()
print(next(perder_vidas))
print(next(perder_vidas))


def generador_multiplos():
    x = 0
    while True:
        yield x
        x += 7


generador = generador_multiplos()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))


def secuencia_infinita():
    x = 0
    while True:
        yield x
        x += 1

generador = secuencia_infinita()

print(next(generador))
print(next(generador))


""" def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x*10)
    return lista

def mi_generador():
    for x in range(1 , 5):
        yield x * 10 #ocupamos menos memoria y retorna cuano solicite


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))
print(next(g)) #va ocupando la memoria y generando a medida que se lo solicite.

def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()

print(next(g))
print(next(g))
#aca podemos seguir creando código y va a responder desde donde quedó
print(next(g))

"""
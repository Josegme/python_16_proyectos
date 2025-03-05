def tiene_doble_cero(*args):
    lista = list(args) #convertimos los argumentos en una lista

    for i in range(len(lista)-1):
        if lista[i] == 0 and lista[i+1] == 0:
            return True

    return False

print(tiene_doble_cero(1, 2, 0, 0, 3, 4))  # True
print(tiene_doble_cero(5, 6, 0, 7, 0))  # False
print(tiene_doble_cero(0, 0))  # True
print(tiene_doble_cero(1, 2, 3, 4, 5))  # False

"""
Explicación del código
*args permite recibir cualquier cantidad de argumentos.
Convertimos args en una lista para facilitar la manipulación.
Usamos un for con range(len(lista) - 1) para recorrer la lista sin desbordarla.
Comparamos cada número con el siguiente → Si ambos son 0, devolvemos True.
Si no encontramos dos ceros seguidos, retornamos False.
"""






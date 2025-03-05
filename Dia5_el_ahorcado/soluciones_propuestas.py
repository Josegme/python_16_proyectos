def devolver_distintos(a,b,c):

    suma = a+b+c
    lista = [a,b,c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort() #ordena a lista de menor a mayor
        return lista[1] #como son 3 numeros el indice 1 es el del medio

print(devolver_distintos(20,5,7))
print(devolver_distintos(3,2,1))
print(devolver_distintos(7,2,4))

#ejercicio 2
def letras_unicas(palabra):
    #vamos a trabajar con una variable SET
    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)
    #los set no estan ordenados
    mi_lista = list(mi_set)
    mi_lista.sort() #para ordenar

    return mi_lista

print(letras_unicas("Entretenido"))

#ejercicio 3

def ceros_vecinos(*args):

    contador = 0
    for num in args:

        if contador + 1 == len(args):
            return False
        if args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1

    return False

print(ceros_vecinos(5,6,8,5,4,9,6,4,3))
print(ceros_vecinos(5,6,8,5,4,9,0,0,6,4,3))

#ejercicio 4

def contar_primos(numero):
    if numero < 2:
        return 0  # No hay primos menores que 2

    primos = [2]  # Lista para almacenar los primos
    iteracion = 3  # Empezamos desde el primer número impar

    while iteracion <= numero:
        es_primo = True  # Suponemos que el número es primo

        for n in range(3, int(iteracion ** 0.5) + 1, 2):  # Solo revisamos impares hasta la raíz cuadrada
            if iteracion % n == 0:
                es_primo = False
                break  # Si encontramos un divisor, dejamos de revisar

        if es_primo:
            primos.append(iteracion)  # Agregamos a la lista de primos

        iteracion += 2  # Solo probamos los números impares

    print("Números primos encontrados:", primos)
    return len(primos)  # Retornamos la cantidad de primos encontrados

# Ejemplo de uso
print("Cantidad total de primos:", contar_primos(50))

"""
✅ Manejamos bien el caso de numero < 2 → Retorna 0 en vez de fallar.
✅ Optimizamos la búsqueda de primos → Solo revisamos divisores hasta √n, mejorando la eficiencia.
✅ Usamos break correctamente → Evita iteraciones innecesarias en la verificación de primos.
✅ No cortamos la función prematuramente → return solo se usa al final, cuando ya tenemos la lista completa de primos.
✅ Evitamos números pares innecesarios → Solo verificamos impares después del 2.
"""

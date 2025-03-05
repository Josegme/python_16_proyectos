def es_primo(num): #creo una funcion para averiguar si es primo
    if num < 2:
        return False #por que 0 y 1 no son primos - entonces el rango arranca desde 2
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True #si no tiene divisories, es primo

def contar_primos():
    numero = int(input('Ingrese un número: '))
    primos = []

    for i in range(2, numero+1):
        if es_primo(i): #llama a la funcion para ver si es primo
            primos.append(i) #agremaos a la lista si es primo

    print("Numeros primos: ", primos)
    return len(primos)

cantidad = contar_primos()
print('Cantidad total de primos: ', cantidad)
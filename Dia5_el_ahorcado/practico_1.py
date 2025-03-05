def devolver_distintos():
    num1 = int(input(f'Ingrese el primer número: '))
    num2 = int(input(f'Ingrese el primer número: '))
    num3 = int(input(f'Ingrese el primer número: '))
    numeros = [num1, num2, num3]
    suma = sum(numeros)

    if suma>15:
        return max(numeros)
    elif suma<10:
        return min(numeros)
    else:
        return sorted(numeros)

#llamamos a la función para mostrar el resultado
resultado = devolver_distintos()
print("Resultado: ", resultado)



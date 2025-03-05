def devolver_palabra():
    palabra = input('Ingrese una palabra: ')
    lista_sin_repetidos = list(dict.fromkeys(palabra))
    return lista_sin_repetidos

resultado = devolver_palabra()
print("Lista de letras sin repetir: ", resultado)
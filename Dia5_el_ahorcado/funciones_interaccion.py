
from random import randint

from random import randint

# Lista de prueba
lista_numeros = [1, 2, 15, 7, 2, 8]

# Función para eliminar duplicados y el mayor valor
def reducir_lista(lista_numeros):
    lista_sin_duplicados = list(set(lista_numeros))  # Elimina duplicados
    max_valor = max(lista_sin_duplicados)  # Encuentra el número más alto
    lista_sin_duplicados.remove(max_valor)  # Lo elimina
    return lista_sin_duplicados  # Devuelve la lista reducida

# Función para calcular el promedio de la lista reducida
def promedio(lista_numeros):
    lista_reducida = reducir_lista(lista_numeros)  # Llama a reducir_lista()
    if len(lista_reducida) == 0:
        return 0  # Evita división por 0
    return sum(lista_reducida) / len(lista_reducida)  # Calcula el promedio

# Llamamos a las funciones en secuencia
lista_reducida = reducir_lista(lista_numeros)
print("Lista reducida:", lista_reducida)

resultado_promedio = promedio(lista_numeros)  # Usa directamente reducir_lista()
print("Promedio:", resultado_promedio)

#función para lanzar dos dados
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1,dado2 #aca devuelve los valores

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1+dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}.Lamentable"
    elif suma_dados < 10: #si entra aca es mayor a 6
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else: #si es >=10
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

dado1, dado2 = lanzar_dados()
resultado = evaluar_jugada(dado1, dado2)
print(resultado)

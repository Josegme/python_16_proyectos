import random

moneda = ['cara', 'cruz']
lista_numeros = [1, 2, 3, 4, 5, 6]

def lanzar_moneda():
    resultado = random.choice(moneda)
    print(f"Moneda lanzada, salió: {resultado}")  # Imprime el resultado antes de retornarlo
    return resultado

def probar_suerte(resultado, numeros):
    print(f"Recibido en probar_suerte: {resultado}")  # Muestra el valor recibido
    if resultado == 'cara':
        print('La lista se autodestruirá')
        return []
    else:
        print('La lista fue salvada')
        return numeros

# Ejecutar el programa
resultado_moneda = lanzar_moneda()  # Lanza la moneda y guarda el resultado
lista_final = probar_suerte(resultado_moneda, lista_numeros)  # Usa el resultado en la segunda función

print('Lista final:', lista_final)



"""import random

# Lista con los posibles resultados de la moneda
moneda = ['cara', 'cruz']

# Lista de números
lista_numeros = [1, 2, 3, 4, 5, 6]

# Función para lanzar la moneda
def lanzar_moneda():
    return random.choice(moneda)

# Función para probar suerte
def probar_suerte(resultado, numeros):
    if resultado == 'cara':
        print('La lista se autodestruirá')
        return []  # Devuelve una lista vacía
    else:
        print('La lista fue salvada')
        return numeros  # Devuelve la lista intacta

# Ejecutar el programa
resultado_moneda = lanzar_moneda()  # Lanza la moneda
lista_final = probar_suerte(resultado_moneda, lista_numeros)  # Prueba suerte

print('Lista final:', lista_final)  # Muestra el estado final de la lista
"""

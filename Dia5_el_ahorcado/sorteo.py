import random
import json

HISTORIAL_FILENAME = "historial_sorteos.json"

def cargar_historial():
    """Carga el historial de sorteos desde un archivo JSON."""
    try:
        with open(HISTORIAL_FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_historial(historial):
    """Guarda el historial de sorteos en un archivo JSON."""
    with open(HISTORIAL_FILENAME, "w") as file:
        json.dump(historial, file, indent=4)

def sortear_numeros():
    """
    Genera un sorteo de 6 números aleatorios entre 00 y 45 sin repetir.
    Retorna una lista con los números sorteados.
    """
    numeros_sorteados = random.sample(range(0, 46), 6)  # Sorteo sin repetición
    numeros_sorteados.sort()  # Ordenamos los números para una mejor visualización
    return numeros_sorteados

def main():
    historial = cargar_historial()
    resultado = sortear_numeros()
    historial.append(resultado)
    guardar_historial(historial)
    print("Números sorteados:", resultado)
    print("Historial de sorteos:", historial)

if __name__ == "__main__":
    main()

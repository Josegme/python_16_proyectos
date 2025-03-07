import os
from pathlib import Path

# Definir la ruta donde se encuentran las recetas
mi_ruta = Path("C:/Equipo120424M/Desktop/GPI_MKT/1_Full_Stack/Python/Dia6_Recetario/Recetas")


# Función para mostrar las categorías disponibles
def mostrar_categorias(ruta):
    categorias = []
    try:
        # Verificar si la ruta existe
        if ruta.exists():
            categorias = [carpeta.name for carpeta in ruta.iterdir() if carpeta.is_dir()]
        else:
            print(f"La ruta {ruta} no existe.")
    except Exception as e:
        print(f"Error al intentar leer las categorías: {e}")
    return categorias


# Función para leer las recetas
def leer_recetas():
    categorias = mostrar_categorias(mi_ruta)
    if categorias:
        print("Categorías disponibles:")
        for categoria in categorias:
            print(f" - {categoria}")
    else:
        print("No hay categorías disponibles.")
    return categorias


# Función para crear una receta nueva
def crear_receta():
    categoria = input("Ingrese la categoría para la nueva receta: ")
    receta = input("Ingrese el nombre de la receta: ")

    categoria_path = mi_ruta / categoria
    if not categoria_path.exists():
        print(f"La categoría {categoria} no existe. Creándola...")
        categoria_path.mkdir(parents=True, exist_ok=True)

    receta_path = categoria_path / f"{receta}.txt"
    with open(receta_path, 'w') as file:
        contenido = input(f"Ingrese el contenido de la receta {receta}: ")
        file.write(contenido)

    print(f"Receta {receta} creada con éxito en la categoría {categoria}.")


# Función para eliminar una receta
def eliminar_receta():
    categoria = input("Ingrese la categoría de la receta a eliminar: ")
    receta = input("Ingrese el nombre de la receta a eliminar: ")

    receta_path = mi_ruta / categoria / f"{receta}.txt"
    if receta_path.exists():
        os.remove(receta_path)
        print(f"Receta {receta} eliminada con éxito.")
    else:
        print(f"La receta {receta} no existe en la categoría {categoria}.")


# Función para eliminar una categoría
def eliminar_categoria():
    categoria = input("Ingrese el nombre de la categoría a eliminar: ")

    categoria_path = mi_ruta / categoria
    if categoria_path.exists():
        try:
            for receta in categoria_path.iterdir():
                receta.unlink()  # Eliminar los archivos de receta
            categoria_path.rmdir()  # Eliminar la carpeta de la categoría
            print(f"Categoría {categoria} eliminada con éxito.")
        except Exception as e:
            print(f"No se pudo eliminar la categoría {categoria}: {e}")
    else:
        print(f"La categoría {categoria} no existe.")


# Función principal para mostrar el menú y ejecutar las acciones
def menu():
    while True:
        print("\n**************************************************")
        print("*****Bienvenido al administrador de recetas*****")
        print("**************************************************")
        print(f"\nLas recetas se encuentran en {mi_ruta}")
        print(f"Total recetas: {sum(1 for _ in mi_ruta.rglob('*.txt'))}")
        print("\nElige una opción:\n")
        print("        [1] - Leer receta")
        print("        [2] - Crear receta nueva")
        print("        [3] - Crear categoría nueva")
        print("        [4] - Eliminar receta")
        print("        [5] - Eliminar categoría")
        print("        [6] - Salir del programa")

        opcion = input()

        if opcion == '1':
            leer_recetas()
        elif opcion == '2':
            crear_receta()
        elif opcion == '3':
            print("Función para crear categoría aún no implementada.")
        elif opcion == '4':
            eliminar_receta()
        elif opcion == '5':
            eliminar_categoria()
        elif opcion == '6':
            print("¡Gracias por usar el administrador de recetas!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")


# Ejecutar el menú
if __name__ == '__main__':
    menu()

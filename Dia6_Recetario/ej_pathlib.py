from pathlib import Path, PureWindowsPath
#purewindowspath transforma una ruta
carpeta = Path("C:/Equipo120424M/Desktop/GPI_MKT/1_Full_Stack/Contenido_Python_Total/dia 6/Prueba.txt")

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
#print(carpeta.read_text()) trae el texto
#print(carpeta.suffix) trae el tipo de archivo .txt
#print(carpeta.stem) #nombre del archivo

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe.")

"""
Pathlib para manipular rutas de sistemas de archivos en cualquier sistema operativo
una de las clases mas importantes de Eclipse y que acabamos de conocer es path
lo hacemos para representar una archivo en el sistema de archivos y que podamos manipularlo
Podemos crear jerarquia de carpetas, y alto grado de legibilidad.

"""
import os
import shutil
#import shend2trash

#print(os.walk())
"""
ejemplo:
ruta = 'C:\\Users\\Wind10\\Desktop\\Carpeta_superior
for carpeta, subcarpeta, archivo in os.walk(ruta): 
    print(f'En la carpeta: {carpeta}')
    print(f'las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{subcarpeta})
    print('Los archivos son: ')
    for arch in archivo:
        print(f'\t{arch}')
    print('\t) 

"""

#si quiero crear un archivo
archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()
print(os.listdir())
#para ver donde estoy
print(os.getcwd())

#para mover archivos utilizo shutil
shutil.move('curso.txt', 'C:\\Equipo120424M\\Desktop')

"""
pip install send2trash 
para enviar todo a la papelera

import send2trash

send2trash.send2trash('curso.txt') 
#manda nuestro archivo a la papelera
"""
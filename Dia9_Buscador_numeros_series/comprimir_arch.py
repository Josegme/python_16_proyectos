import shutil

#tambien podemos utilizar para administrar y manipular las carpetas
carpeta_origen = #Ruta de nuestra carpeta

archivo_destino = "Todo comprimido"

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

"""
import zipfile

mi_zip = zipfile.ZipFile('archivo_comprimido', 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()

zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()
"""


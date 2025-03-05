# r = solo lectura
# w = solo escritura
# a = podemos escribir
#from Dia6_Recetario.entrada_salida_1 import mi_archivo

mi_archivo = open('Prueba.txt', 'w')
mi_archivo.write('Nuevo Texto')
mi_archivo.close()
mi_archivo = open('Prueba.txt', 'r')
print(mi_archivo)
mi_archivo.close()
"""
archivo = open('prueba.txt', 'r') # open(parametro archivo de texto, parametro que voy a operar)
archivo.write('soy el nuevo texto') #no va a poder escribir por que esta en solo lectura

archivo1 = open('prueba1.txt', 'w') #hace que el texto se regenere y modifique por completo
#es decir sobre escribe lo que estaba en el texto
archivo1.write('Hola ')
archivo1.write('Mundo!')
archivo1.write('''Esto 
es un salto
de linea''')
# archivo1.writelines(['Hola','Mundo','Aqui','estoy'])

archivo = open('Prueba.txt', 'a')
archivo.write('. Bienvenido!')

archivo.close()
"""

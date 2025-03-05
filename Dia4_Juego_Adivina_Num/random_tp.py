#random e importanción de libreria
from random import *
#mejor es cambiar el nombre del archivo que no sea igual que la libreria
aleatorio = randint(1,50)
print(aleatorio) #va a ir tomando o arrojando un num distinto
aleatorio_uni = round(uniform(1,5),2)
print(aleatorio_uni) #con round redondeo el valor comprendido que estoy buscando
aleatorio_rand = random() #numeros aleatorios entre 0 y 1
print(aleatorio_rand)
colores = ['azul','rojo','verde','amarillo']
aleatorio_choi = choice(colores)
print(aleatorio_choi) #va a seleccionar aleatoriamente de la lista
#shuffle
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros) #va a ir ordenando de manera distinta. modifica a la lista.

prueba = random()
print(prueba)
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)
"""
class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro', 'Tucán')

print(mi_pajaro.color)
print(mi_pajaro.especie)
print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')

print(Pajaro.alas)
print(mi_pajaro.alas)
"""
from Dia7_OpBancaria.clase import harry_potter


class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano', True, 17)

print(harry_potter.especie)

class Cubo:

    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')
print(cubo_rojo.color)

class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('blanco', '4')

print(f'Mi casa es {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos}')
"""class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('Pío, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro ha volado {metros} mts.')

piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(50)"""

class Alarma:

    def postergar(self, cantidad_minutos):
        print(f'La alarma ha sido pospuesta {cantidad_minutos} minutos')

despertador = Alarma()
despertador.postergar(15)




class Mago:

    def lanzar_hechizo(self):
        print('¡Abracadabra!')

merlin = Mago()
merlin.lanzar_hechizo()


class Perro:

    def ladrar(self):
        print('Guau!')

mi_perro = Perro()
mi_perro.ladrar()


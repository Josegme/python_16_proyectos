class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('Pío')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} mts.')
        self.piar()

    def pintar_netro(self):
        self.color = 'Negro'
        print(f'Ahora el pajaro es {self.color}')

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos.")
        #print(f'Es de color {self.color}') #no puede tomar el atributo.
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod #no se pueden relacionar con las instancias ni accend a los atributos de clase
    def mirar():
        print("El pajaro mira")

Pajaro.mirar()


Pajaro.poner_huevos(5) #los metodos no necesitan una instancia para ejecutarse
#pero no pueden acceder a los atributos por ejemplo color o especie




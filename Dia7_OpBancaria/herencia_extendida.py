#herencia multiple
class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('jajajajaj')

    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
#siempre hereda en orden de busqueda por jerarquia siguiendo el orden de la herenci
print(Nieto.__mro__) #method order resolution
#nieto > hijo > padre > madre > object


"""class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(selfs):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(selfs):
        print('Pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} mts.')

piolin = Pajaro(3, 'Amarillo', 300)
mi_animal = Animal(5, negro)


piolin.nacer()
piolin.hablar() #si bien hablar es hereddo se modifico por su propio metodo en la misma clase
piolin.volar(100) #puede tener su propio metodo
#pueden tener atributos propios de los pajaros que no sea de Animal
"""
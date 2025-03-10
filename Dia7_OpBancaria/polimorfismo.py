class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

#funcion que recibe cualquier objeto y ejecuta el método defender
def defender_personaje(personaje):
    personaje.defender()

mago = Mago()
arquero = Arquero()
samurai = Samurai()

defender_personaje(mago)
defender_personaje(samurai)


class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

arquero = Arquero()
mago = Mago()
samurai = Samurai()

personajes = [arquero, mago, samurai]

for personaje in personajes:
    personaje.atacar()


#polimorfismo (muchas formas que pueden tomar los objetos)
"""objetos de diferentes class pueden compartir los mismos metodos
y luego pueden llamar desde el mismo lugar

class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice Muuu')

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice Meee')

#creamos una instacia/objeto para cada clase

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')
#pueden ejecutar cosas distintas aunque tienen métodos con el mismo nombre
vaca1.hablar()
oveja1.hablar()
animales = [vaca1, oveja1]

for animal in animales: #llamamos de la misma manera en un Loop a objetos que hacen cosas disntintas
    animal.hablar()

def animal_habla(animal):
    animal.hablar()
#si comparten el mismo nombre del metodo podemos iterear con objetos con metodos con mismo nombre
#que realicen diferentes cosas
animal_habla(vaca1)
animal_habla(oveja1)

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)
#creamos una lista de obejetos
objetos = [palabra, lista, tupla]
for obj in objetos:
    print(f"El objeto {obj} tiene una longitud de {len(obj)}")"""
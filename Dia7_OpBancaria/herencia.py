class Mascota:
    def __init__(self,edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

perrito = Perro(5, 'Frodo', 4)

print(perrito.edad)




class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

alumno1 = Alumno('Juan Perez', 21)

print(alumno1.nombre)

class Animal:
    def __init__(self, edad, color): #atributos de clase
        self.edad = edad
        self.color = color

    def nacer(selfs):
        print("Este animal ha nacido.")

class Pajaro(Animal):
    pass


piolin = Pajaro(2, 'Amarillo')

print(piolin.color)


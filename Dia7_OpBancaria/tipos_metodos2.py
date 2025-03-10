class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas  # Atributo de instancia

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1  # Restamos una flecha
            print(f'Flecha lanzada. Flechas restantes: {self.cantidad_flechas}')
        else:
            print('No quedan más flechas.')

# Crear un personaje con 3 flechas
arquero = Personaje(3)

# Llamamos al método varias veces
arquero.lanzar_flecha()  # Dispara 1 flecha
arquero.lanzar_flecha()  # Dispara otra
arquero.lanzar_flecha()  # Última flecha
arquero.lanzar_flecha()  # Ya no quedan flechas




class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas #atributo de instancia

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -=1
            print(f'Flecha lanzada. Flechas Restantes: {self.cantidad_flechas}')
        else:
            print('No quedan flechas')

    def cargar_flechas(self):
        if self.cantidad_flechas == 0:
            self.cantidad_flechas += 5
            print(f'Recargado con {self.cantidad_flechas} Flechas!')
        else:
            print('Aún tienes flechas.')

arquero = Personaje(5)

arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()
arquero.lanzar_flecha()


arquero.cargar_flechas()





class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()

class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True #cambia el atributo de clase

print(Jugador.vivo)
Jugador.revivir()
print(Jugador.vivo)


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

piolin = Pajaro("Amarillo", "Canario")
print(piolin.color)
piolin.pintar_netro() #es decir que el método de instancia modifico el atributo
piolin.volar(50) #los metodos de instancias pueden invocar otros métodos

piolin.alas = False
print(piolin.alas) #pude modificar algo que correspondia a la clase


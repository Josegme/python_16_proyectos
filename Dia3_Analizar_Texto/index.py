#index() -> se utiliza para conocer la posicion o indicie de un caracter dentro de un string
print("Buscamos una Letra con index()")
mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
resultado2 = mi_texto[9]
resultado3 = mi_texto[-4]
print(resultado)
print(resultado2)
print(resultado3)
#ahora buscamos el indice
print("Ahora queremos saber el indice de un string-la posición")
resultado4 = mi_texto.index("n")
resultado5 = mi_texto.index("prueba")
#solo busca de izq a derecha, pero podemos buscar desde un punto determinado
resultado6 = mi_texto.index("a")
resultado7 = mi_texto.index("a", 5)
resultado8 = mi_texto.index("a", 11, 18)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print("Podemos buscar en reversa con .rindex")
resultado9 = mi_texto.rindex("a")
print(resultado9)
print("Ejercicios de Clase:")
palabra = "ordenador"
resultado_ej1 = palabra[4]
print(resultado_ej1)
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("p")
print(resultado)
resultado = frase.rindex("p")
print(resultado)
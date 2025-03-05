#fragmentar cadenas slicing(i:f)
from Dia3_Analizar_Texto.index import resultado5

texto = "ABCDEFGHIJKLMN"
fragmento = texto[2:5]
fragmento1 = texto[2:]
fragmento2 = texto[:5]
#para extraer todo desde el indicie 2 hasta antes del 5
print(fragmento)
print(fragmento1)
print(fragmento2)
print("Podemos agregar un tercer factor de busqueda")
fragmento3 = texto[2:10:3]
fragemento4 = texto[::3]
fragemento5 = texto[::-3]
print(fragmento3)
print(fragemento4)
print(fragemento5)
print("Ejercicios de Clase")
frase = "Controlar la complejidad es la esencia de la programación"
fragmento_ej = frase[0:9]
print(fragmento_ej)
frase1 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento_ej1 = frase1[9::3]
print(fragmento_ej1)
frase3 = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento_ej3 = frase3[::-1]
print(fragmento_ej3)
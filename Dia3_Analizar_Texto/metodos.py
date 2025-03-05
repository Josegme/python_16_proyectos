#métodos de Strings
"""
texto = "Este es el texto de Federico"

mayuscula = texto.upper()
minuscula = texto.lower()
mayus_indice = texto[2].upper()
met_split = texto.split()
#con split puedo elegir un separador
met_split2 = texto.split("e")

print(mayuscula) #imprime todo el texto en mayuscula
print(mayus_indice) #imprime T mayuscula por que esta en el indice 2
print(minuscula)
print(met_split)
print(met_split2)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d]) #espacio para separar a estas palabras
print(e)

buscar = texto.find("s")
buscar1 = texto.find("Federico")
print(buscar)
print(buscar1)

reemplazar = texto.replace("Federico", "Gustavo")
print(reemplazar)
reemplazar_letras = texto.replace("e", "x")
print(reemplazar_letras)

print("Ejercicios de clase")

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
mayusculas = frase.upper()
print(mayusculas)
lista_palabras = ["La","legibilidad","cuenta."]
unir = " ".join(lista_palabras)
print(unir)"""
frases = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase_modificada = frases.replace("difícil", "fácil").replace("mala", "buena")
print(frase_modificada)
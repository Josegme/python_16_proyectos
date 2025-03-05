#primero pensar en las variables que vamos a necesitar
texto = input("Ingresa un texto a elección: ")
letra = [] #generamos una lista vacia para reservar las letras
#ahora transformamos el texto en minusculas
texto = texto.lower()
#el usuario debe ingresar la letras
letra.append(input("Ingresa la primera letra ").lower()) #para que se agregue al indice
letra.append(input("Ingresa la segunda letra ").lower())
letra.append(input("Ingresa la terecera letra ").lower())
#ahora me quiero asegurar que todo este en minuscula
print("\n")
print("Cantidad de letras")
cantidad_letras1 = texto.count(letra[0])
cantidad_letras2 = texto.count(letra[1])
cantidad_letras3 = texto.count(letra[2])

print(f"Hemos encontrado la letra {letra[0]} repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra {letra[1]} repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra {letra[2]} repetida {cantidad_letras3} veces")

print("Cantidad de Palabras")
palabras = texto.split() #para contar las palabras
print(f"Hemos encontrado {len(palabras)} en tu texto ")

print("Letras de incio y de fin")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"la letra incial es '{letra_inicio}' y la letra final '{letra_final}'")
print("Texto Invertido")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos el texto al revés va a decir: '{texto_invertido}'")

print("\n")
print('Buscando la palabra Python')
buscar_python = 'python' in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
#Min y Max: para buscar valores máximos y mínimo de una colección.

coleccion1= min(35,20,8,10,36,89,101)
coleccion2 = max(35,20,8,10,36,89,101)

print(coleccion1)
print(coleccion2)

lista = [58,96,72,64,35]
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')
#coleccionable, variable, tuple.

#los str son ordenables alfabeticamente
nombre = ['Juan','Pablo','Alicia','Carlos']
print(min(nombre)) #tener en cuenta que busca primero en MAYUSCULAS
nombre1 = 'Carlos'
print(min(nombre1)) #si bien la es la primera de abecedario C es mayuscula y esta primero
print(min(nombre1.lower()))

#como se comporta con los diccionarios.
dic = {'C1':45,'C2':11}
print(min(dic)) #pero para pedir el valor mas pequeño debo utilizar el met values
print(min(dic.values())) #de esta manera me devuelve el valor y no la clave

print('Ejercicios')
#ejercicio1
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)
#ejercicio2
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
maximo = max(lista_numeros)
minimo = min(lista_numeros)
rango = maximo - minimo
print(rango)
#ejercicio 3
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
#print(min(dic.values()))
print(edad_minima)
ultimo_nombre = max(diccionario_edades)
print(ultimo_nombre)

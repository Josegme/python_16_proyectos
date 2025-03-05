nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]

combinados = list(zip(nombres, edades))
print(combinados)
#zip llega al largo de la lista mas corta y
#pueden ser dos o mas listas
ciudades = ['Lima','Perú','México']
cominados1 = list(zip(nombres, edades, ciudades))
print(cominados1)

#cual es la utilidad?
for nombre,edad,ciudad in cominados1:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')

print('Ejercicios')
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

ciudad_pais = list(zip(capitales, paises))

for capital, pais in ciudad_pais:
    print(f'La capital de {pais} es {capital}')

espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espanol, portugues, ingles))
print(numeros)


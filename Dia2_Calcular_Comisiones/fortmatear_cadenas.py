#formateamos cadenas
"""
color = "Rojo"
matricula = 541926
#utilizamos f para las cadenas literales
print(f"El auto es {color} y su matricula es {matricula}")


x = 10
y = 5

print("Mis números son {} y {} ".format(x, y))
print("La suma de {} y {} es igual a {}".format(x,y, x+y))
"""
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058

print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

puntos_nuevos = 350
puntos_totales = 1225

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos.")

puntos_anteriores = 875
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos, puntos_nuevos+puntos_anteriores))
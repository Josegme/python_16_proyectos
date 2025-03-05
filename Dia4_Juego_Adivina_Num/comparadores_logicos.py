#operadores lógicos and or not
mi_bool = 4<5<6
print(mi_bool)
mi_bool = 4<5 and 5>6
print(mi_bool)
mi_bool = (4<5) and (5==2+3)
print(mi_bool)
#comparaciones con distintos tipos
#no importa si las comparaciones son de una u otra naturaleza
mi_bool = (55==55) and ('perro'=='perro')
print(mi_bool)
#para comparar con or
mi_boolor = 10==10 or 3==3
print(mi_boolor)
mi_boolor = 1==10 or 3==3
print(mi_boolor) #por que si V v F = V con que una sea verdadera ya es V
texto = "esta frase es breve"
mi_bool = 'frase' in texto
print(mi_bool)
mi_bool = ('frase' in texto) and ('python' in texto)
print(mi_bool)

print('not')
mi_boolnot = not ('a' == 'a')
print(mi_boolnot)
mi_boolnot = not ('a' != 'a')
print(mi_boolnot)

print('Ejercicios')
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = (num1>num2) and (num1<num3)
print(mi_bool)
mi_bool = (num1>num2) or (num1<num3)
print(mi_bool)
#ejercicio 3
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = not (palabra1 in frase) and not (palabra2 in frase)
print(mi_bool)
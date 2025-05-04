"""
Los comentarios y docstring son utilizados como buena práctica para 
la documentación del programa que se esta desarrollando.
"""

# identación en Python

x = [0,1,2,3,4]

for i in x: 
    item = x[i]
    print('x es igual a', x[item])
    print('Hola mundo por ', i, ' vez.')



edad = 18  # edad mínima de la persona

def meses(años):
    """ Esta funcion permite calcular la edad en meses"""
    return años*12

print(meses(edad))
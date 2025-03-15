"""
from collections import [elemento]
el módulo nos permite manejar las estructuras de datos de manera mas 
eficiente. 
counter-defaultdict-namedtuple
"""
from collections import Counter
from collections import defaultdict
from collections import namedtuple

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)

print(ariel.nombre)
print(ariel.altura)
print(ariel[2])


#defaultdict
mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = 'verde'
print(mi_dic['dos'])

print(mi_dic)


#Counter
serie = Counter([1,1,1,1,1,1,2,2,2,2,3,53,3,3,4])
print(serie.most_common())
print(serie.most_common(2))
print(list(serie))

numeros = [8,6,9,5,4,5,5,5,5,5,8,7,4,5,6,4]
frase = 'al pan pan y al vino vino'
print(Counter('missisisipi'))
print(Counter(frase))
print(Counter(frase.split()))






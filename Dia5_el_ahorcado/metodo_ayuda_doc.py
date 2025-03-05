print('Ejercicios')

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(1, "naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

metodo = marcas_smartphones.isdisjoint(marcas_tv)
print(metodo)

"creamos la cadena"
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
#eliminamos los caracteres especificos del lado izquierod
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
resultado = texto.lstrip(', : % _ #')
print(resultado)
resultado = texto.lstrip(",:_#%")
#imprimimos el resultado
print(resultado)
text = 'Arthur: three!'
text1 = 'Elena: de la Ostia'
resultado = text.lstrip('Arthur: ')
resultado1 = text1.removeprefix('Elena: ')
print(resultado)
print(resultado1)





"""
dic = {'clave1': 100,
       'clave2': 500,
       'clave3': 700
       }
a = dic.popitem()
print(a)
print(dic)
"""
#diccionarios
#ejercicios
mi_dic = {
    'nombre': 'Karen',
    'apellido': 'Jurgens',
    'edad': 35,
    'ocupacion': 'Periodista'
}
print(mi_dic)
mi_dict1 = {"valores_1":{"v1":3,
                         "v2":6},
            "puntos":{"points1":9,
                      "points2":[10,300,15]
                      }
            }
print(mi_dict1["puntos"]["points2"][1])
#ejercicio3
mi_dic = {"nombre":"Karen",
          "apellido":"Jurgens",
          "edad":35,
          "ocupacion":"Periodista"
          }
mi_dic["edad"]=36
mi_dic["ocupacion"] = "Editora"
mi_dic["Pais"] = "Colombia"
print(mi_dic)

"""
diccionario ={
    'c1': 'Valor1',
    'c2': 'Valor2'
}
print(diccionario)
resultado = diccionario['c1']
print(resultado)
#tengo un objeto cliente
cliente = {
    'nombre' : 'Juan',
    'apellido' : 'Fuentes',
    'peso' : 88,
    'talla' : 1.76
}
#quiero hacer una consulta
consulta = cliente['apellido']
consulta1 = cliente['talla']
print(consulta)
print(consulta1)

#podemos colocar dentro del diccionario todo tipo de datos
dicc = {
    'clave1': 55,
    'clave2': [10,20,30],
    'clave3': {'s1':100, 's2':200}
}
print(dicc['clave2'][1])
print(dicc['clave3'])
#ejercicio
dic = {
    'cl1':['a','b','c'],
    'cl2':['d','e','f']
}
print(dic['cl2'][1].upper())
print(dic)
dic['cl3'] = ['g', 'h']
print(dic)
#para sobre escribir
dic['cl1'] = ['A','B',5]
print(dic)
#para conocer todas las claves
print(dic.keys())
print(dic.values())
print(dic.items())
"""
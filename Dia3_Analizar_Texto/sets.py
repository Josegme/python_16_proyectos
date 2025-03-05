#ejercicios
#union de sets
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)
#eliminar un elemento
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

#agregar nombre
sorteo.add("Damián")
print(sorteo)
sorteo.pop()
print(sorteo)

"""mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3}
print(type(otro_set))
print(otro_set)

#los sets no tienen orden interno
#por lo tanto no se puede modificar elementos ni cambiar ni reasignar
mi_set2 = set([11,1,1,1,1,1,2,(1,2,3),2,2,2,0,00,3,3,3])
print(mi_set2) #no se pueden repetir elementos y ordena por default
#no admite list ni dic pero si tuple por que son inmutables
print(len(mi_set2))
print(2 in mi_set2)
#se pueden hacer union de sets
s2 = {2, 3, 4, 5}

s3_union = mi_set2.union(s2)
print(s3_union)

s2.add(6) #se agrega solo si no existe dentro del set
s2.remove(3)
s2.discard(8)
s2.pop() #elimina un elemento aleatorio es peligroso pero sirve par aun sorteo por ejemplo
s2.clear()
print(s2)
#existen otros metodos.
"""

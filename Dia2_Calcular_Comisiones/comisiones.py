nombre = input("Por favor, dime tu nombre: ")
ventas =  input("Diga sus ventas totales del mes: ")

ventas = int(ventas)

comision = ventas * 13/100
comision = round(comision)

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
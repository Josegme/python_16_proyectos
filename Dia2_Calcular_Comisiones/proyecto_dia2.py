
nombre = input("Escribe tu nombre: ")
ventas = float(input("Escribe el total de ventas: "))

print(f"Hola {nombre}, el total de ventas es ${ventas}.")

comision = round(ventas*0.13, 2)


print(f"Hola {nombre}, Tu comision por el total de ventas es {comision}")


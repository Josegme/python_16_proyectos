#ejercicios
num1 = "1.75"
num2 = "10"
num1 = float(num1)
num2 = int(num2)
print(num1 + num2)


num2 = 10
num2 = float(num2)
print(type(num2))

num1_ej1 = 1.75
num1_ej1 = int(num1_ej1)
print(type(num1_ej1))

"""
#conversiones implicitas
num1 = 20 #tipo int
num2 = 30.5 #tipo float

num1 = num1 + num2

print(type(num1)) #num1 va a pasar a ser float para que se ejecute la suma
print(type(num2))

#conversiones explicitas
num11 = 5.8
print(num11)
print(type(num11))
#si quiero transformar la variable num11 a integer
num22 = int(num11)
print(num22)
print(type(num22))
#imprime 5 -> no redondea sino que elimina la parte decimal

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))

nueva_edad = 1 + edad
print(nueva_edad)
"""
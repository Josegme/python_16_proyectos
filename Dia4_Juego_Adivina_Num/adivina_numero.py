from random import randint

nombre = input('Dime cuál es tu nombre: ')
numero_aleatorio = randint(1, 100)
# print(numero_aleatorio)  # Descomenta esto para ver la respuesta oculta.

print(f'Bueno, {nombre}, he pensado en un número entre 1 y 100, y '
      f'tienes ocho intentos para adivinar cuál crees que es el número.')

intentos = 0

while intentos < 8:
    try:
        num_usuario = int(input('Ingresa el número: '))
        intentos += 1

        if num_usuario < 1 or num_usuario > 100:
            print('Has elegido un número no permitido. Vuelve a ingresar otro número.')
        elif num_usuario < numero_aleatorio:
            print('Respuesta incorrecta, has elegido un número menor. Vuelve a intentarlo.')
        elif num_usuario > numero_aleatorio:
            print('Respuesta incorrecta, has elegido un número mayor. Vuelve a intentarlo.')
        else:
            print(f'¡Has ganado en {intentos} intentos! 🎉')
            break  # Sale del bucle si acierta
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Mensaje si se agotaron los intentos
if intentos == 8 and num_usuario != numero_aleatorio:
    print(f'Lo siento, {nombre}. Has agotado tus intentos. El número era {numero_aleatorio}.')

print('Gracias por jugar. ¡Vuelve pronto!')

"""from random import randint

nombre = str(input('Dime cual es tu nombre: '))
numero_aleatorio = randint(1,100)
#print(numero_aleatorio)
print(f'Bueno, {nombre} he pensado en un número entre 1 y 100, y '
      f'tienes ocho intentos para adivinar cual crees que es el número.')

intentos = 0

while intentos < 8:
    num_usuario = int(input('Ingresa el número: '))
    intentos +=1
    if num_usuario < 1 or num_usuario > 100:
        print('Haz elegido un número no permitido, vuelve a ingresar otro número')
    elif num_usuario < numero_aleatorio:
        print('Respuesta incorrecta, haz elegido un numero menor. Vuelve a intenarlo')
    elif num_usuario > numero_aleatorio:
        print('Respuesta incorrecta, haz elegido un número mayor. Vuelve a intentarlo')
    elif num_usuario == numero_aleatorio:
        print(f'Haz Ganado!!! con {intentos} . Muy bien!')
        break
    else:
        print('Lo siento! haz completado el numero de intentos.')

print('Gracias por jugar. Vuelve pronto. ')"""






#funciones dinámicas
from Dia4_Juego_Adivina_Num.loop_for import lista_numeros


def chequear_3_cifras(numero):
    return numero in range(100,1000)

suma = 586+402
resultado = chequear_3_cifras(suma)
print(resultado)

#quiero que cheque los numeros de una lista y ver si es verdad que esos numeros tienen tres cifras

def chequear_3cifras_lista(lista):

    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass #para que siga recorriendo y controlando la lista.

    return False

resultado = chequear_3cifras_lista([55,99,6000])
print(resultado)
#devuelve >none si no encuentra
#si encuentra es True
#y asi va recorriendo hasta que termine.
#como hacer que nos devuelva False si no encuentra ningun valor True

def checar_cifras(lista1):
    lista_cifras_checadas = []
    for n in lista1:
        if n in range(100,1000):
            lista_cifras_checadas.append(n)
        else:
            pass
    return lista_cifras_checadas

resultado = checar_cifras([55,999,455,13,8461,101])
print(resultado)

print("Ejercicios")

def todos_positivos(lista):
    for n in lista:
        if n<0:
            return False

    return True

lista_numeros = [2,3,6,8,9,10]
resultado = todos_positivos(lista_numeros)
print(resultado)

def suma_menores(lista):
    num = 0
    for n in lista:
        if 0<n<1000:
            num += n
    return num


lista_numeros = [10,15,25]
resultado = suma_menores(lista_numeros)
print(resultado)

def cantidad_pares(lista):
    par = 0
    for n in lista:
        if n%2 == 0:
            par +=1
    return par

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
resultado = cantidad_pares(lista_numeros)
print(resultado)



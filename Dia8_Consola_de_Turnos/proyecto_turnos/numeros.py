def numeros_perfumeria():
    for n in range(1, 10000):
        yield f'Perf - {n}'

def numeros_farmacia():
    for n in range(1, 10000):
        yield f'Farm - {n}'

def numeros_cosmetica():
    for n in range(1, 10000):
        yield f'Cosm - {n}'

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(rubro):

    print('\n' + '*'*23)
    print('Su número es: ')
    if rubro == 'P':
        print(next(p))
    elif rubro == 'F':
        print(next(f))
    else:
        print(next(c))
    print('Aguarde y sera antendido')
    print('*'*23, '\n')
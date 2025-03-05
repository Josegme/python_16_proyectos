#coincidencia de patrones estructurales
serie = "N02"
#otros lenguajes switch o case
#en python utilizamos match elige una opcion entre varias pero ademas cumple con otras funciones
match serie:
    case "N01":
        print("Samsung")
    case "N02":
        print("Nokia")
    case "N03":
        print("Motorola")
    case _:
        print("No existe ese producto")

cliente = {
    'nombre': 'Federico',
    'edad':45,
    'ocupacion': 'instructor'
}

pelicula = {'titulo':'Matrix',
            'ficha_tecnica': {
                    'protagonista': 'Keanu Reeves',
                    'director': 'Lana y Lily'}
            }
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre,edad,ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica':{'protagonista':protagonista,
                               'director':director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No se que es esto")
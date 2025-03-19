import re

def verificar_cp(codigo_postal):
    patron = r'^[A-Za-z0-9]{2}[0-9]{4}$'

    if re.match(patron, codigo_postal):
        print("OK")
    else:
        print("El código no es correcto")

verificar_cp("AB1234")
verificar_cp("AB11")
verificar_cp("ABCD2")


def verificar_saludo(frase):
    patron = r'^Hola\b'

    if re.match(patron, frase):
        print("OK")
    else:
        print("No has saludado")

frase = "como estas?"
print(verificar_saludo(frase))
#^Hola\b verifica que la frase empiece exactamente con "Hola" como palabra completa.
#\b es un límite de palabra, evita coincidencias parciales como "Holanda".



def verificar_email(email):
    patron = r'^[^@]+@[^@]+\.(com)(\.\w+)?$'

    if re.match(patron, email):
        print('ok')
    else:
        print('La dirección de email es incorrecta')

#ejemplo
verificar_email('usuario@gmail.com')
verificar_email('usuario@yahoo.com.br')
verificar_email('usuario@ejemplo.org')
"""

texto = "llama al 564-658-6588 ya mismo"

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron1 = r'\d{3}-\d{3}-\d{4}'
patron3 = re.compile(r'\d{3}-\d{3}-\d{4}')

resultado = re.search(patron, texto)
print(resultado)

resultado2 = re.search(patron1, texto)
print(resultado2.group())

texto = "Si necesitas ayuda llama al (658)-598-997 las 24 horas al servicio online"

patron = 'ayuda'

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())


patron = 'llama'
patron2 = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda.span())
busqueda2= re.search(patron2, texto)

print(busqueda2.end())
busqueda3 = re.findall(patron, texto)
print(len(busqueda3))
"""


"""
expresiones regulares que requiero buscar o utilizar
re = regular expresion
from Dia6_Recetario.directorios2 import carpeta

patro = r'\d\d\d-\d\d\d-\d\d\d\d'
patron = r'\d{3}-\d{3}-\d{4}'
#caracteres especiales para construir patrones
/d      descripcion v\d.\d\d
/w      caracter alfanumerico \w\w\w-\w\w
/s      espacio en blanco número\s\d\d
/D      No numérico \D\D\D\D
abcd AbCd AB-C abc?
/W      no alfanumérico
/S
#cuentificadores para no repetir
car     descripcion ejemplo
1       1 o más veces código_ \d-\d+
{n}     se repite n veces \d-\d{4}
{n,m}   se repite de n a m veces \w{3, 5}
{n, }   desde n hacia arriba    -\d{4, }-
*       significa 0 o mas \w\s*\
"""








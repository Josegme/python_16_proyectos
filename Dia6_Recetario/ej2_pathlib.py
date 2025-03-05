from pathlib import Path

base = Path.home()
ruta_base = Path(base,"Cursos")
print(ruta_base)
"""
guia = Path("Barcelona","Sagrada_Familia.txt")
print(guia)
#contiene una ruta relativa o sea que puede tener varias direcciones
#si fuera una ruta absoluta tendriamos una direccion especifica
base = Path.home() #devuelve una instancia path con ruta absoluta
guia2 = Path(base,"Brasil", "Marketing.txt")
print(base)
print(guia2)
guia3 = guia.with_name("La_Pedredra.txt")
print(guia3)
#acepta cadenas como objetos de path
print(guia.parent) #podemos seleccionar diferentes niveles de la ruta

for txt in Path(guia).glob("**/*.txt"):
    print(txt)

guia = Path("Europa","España","Barcelona","Sagrada_familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_españa = guia.relative_to(Path("Europa","España"))
print(en_europa)
print(en_españa)
"""
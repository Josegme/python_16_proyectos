"""para manipular datos de tiempo"""
from datetime import datetime

minutos = datetime.now().minute
print(minutos)



"""
nacimiento = date(1995, 5, 5)
defuncion = date(2095, 6, 19)

vida = defuncion - nacimiento
print(vida.days)

from datetime import datetime

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)
vigilia = duerme - despierta
print(vigilia.seconds)

mi_fecha = datetime(2025, 5, 22, 15)
mi_fecha = mi_fecha.replace(month = 11)


print(mi_fecha)
"""
"""
import datetime

mi_dia = datetime.date(2025, 2, 22)
print(mi_dia)
print(mi_dia.today())
print(mi_dia.year)
print(mi_dia.ctime())

mi_hora = datetime.time(17, 35, 56)
print(mi_hora)
#podemos imprimir elementos del tiempo
print(mi_hora.hour)
"""



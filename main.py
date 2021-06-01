import psycopg2 as p
import sys
from datetime import datetime
from datetime import timedelta
from datetime import date

from funciones import *
from queries import *

#planteamiento

print("Iniciando programa...")
print("Revision de accesos al aparcamiento del Palacio de Buenavista")

print(espacio)

print("Resultado fecha: " + start_date())
resultado_lista_matriculas = (consultador(start_date(), query_lista_matriculas))
print("Total accesos: " + str(resultado_lista_matriculas[0][0]))
resultado_lista_distinct_matriculas = (consultador(start_date(), query_lista_distinct_matriculas))
print("Total vehiculos distintos: " + str(resultado_lista_distinct_matriculas[0][0]))

print(espacio)

resultado_historico_total_matriculas = []
resultado_historico_distinct_matriculas = []

numero = 0
while numero < 25:
    numero += 7
    print("Resultado fecha: " + resta_fecha(numero))
    consulta_total_matriculas = consultador(resta_fecha(numero), query_lista_matriculas)
    resultado_historico_total_matriculas.append(int(consulta_total_matriculas[0][0]))
    print("Total de accesos: " + str(consulta_total_matriculas[0][0]))

    consulta_matriculas_distintas = consultador(resta_fecha(numero), query_lista_distinct_matriculas)
    resultado_historico_distinct_matriculas.append(int(consulta_matriculas_distintas[0][0]))
    print("Total vehiculos distintos: " + str(consulta_matriculas_distintas[0][0]))
    print(espacio)


#sacar media
media_total_matriculas = (sum(resultado_historico_total_matriculas)/4)
media_distinct_matriculas = (sum(resultado_historico_distinct_matriculas)/4)

#comparar % accesos del día
ratio_total_matriculas = (int(resultado_lista_matriculas[0][0]) * 100)/media_total_matriculas
ratio_matriculas_distintas = (int(resultado_lista_distinct_matriculas[0][0]) * 100)/media_distinct_matriculas
print(ratio_total_matriculas)
print(ratio_matriculas_distintas)

# comparar cuantas veces leemos un vehiculo

print("¿cuantas hemos leido los vehículos el " + start_date() + "? Debería ser, al menos cercano, a 2 o superior.")
ratio_lectura = (resultado_lista_matriculas[0][0]/resultado_lista_distinct_matriculas[0][0])
print(type(ratio_lectura))
#print(ratio_lectura[0:5])
print(round(ratio_lectura, 2))
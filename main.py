import psycopg2 as p
import sys
from datetime import datetime
from datetime import timedelta
from datetime import date

from funciones import *
from queries import *


# Instrucciones: Insertar la fecha como argumento del dia que se quiera realizar la busqueda

#planteamiento

print("Iniciando programa...")
print("Revision de accesos al aparcamiento del Palacio de Buenavista")

print(espacio)

print("Resultado fecha: " + start_date())
resultado_lista_matriculas = (consultador(start_date(), query_lista_matriculas))
print("Total accesos: " + str(resultado_lista_matriculas[0][0]))
resultado_lista_distinct_matriculas = (consultador(start_date(), query_lista_distinct_matriculas))
print("Total vehiculos distintos: " + str(resultado_lista_distinct_matriculas[0][0]))


resultado_historico_total_matriculas = []
resultado_historico_distinct_matriculas = []

numero = 0
while numero < 25:
    numero += 7
    consulta_total_matriculas = consultador(resta_fecha(numero), query_lista_matriculas)
    resultado_historico_total_matriculas.append(int(consulta_total_matriculas[0][0]))

    consulta_matriculas_distintas = consultador(resta_fecha(numero), query_lista_distinct_matriculas)
    resultado_historico_distinct_matriculas.append(int(consulta_matriculas_distintas[0][0]))


#sacar media
media_total_matriculas = (sum(resultado_historico_total_matriculas)/4)
print("Media total de accesos: " + str(media_total_matriculas))
media_distinct_matriculas = (sum(resultado_historico_distinct_matriculas)/4)
print("Media de vehiculos distintos: " + str(media_distinct_matriculas))

#comparar % accesos del día
ratio_total_matriculas = (int(resultado_lista_matriculas[0][0]) * 100)/media_total_matriculas
ratio_matriculas_distintas = (int(resultado_lista_distinct_matriculas[0][0]) * 100)/media_distinct_matriculas
print("Ratio total de accesos: " + str(round(ratio_total_matriculas, 2)))
#print("Ratio de vehiculos distintos: " + str(round(ratio_matriculas_distintas, 2)))

# comparar cuantas veces leemos un vehiculo
print("¿cuantas hemos leido los vehículos el " + start_date() + "? Debería ser, al menos cercano, a 2 o superior.")
ratio_lectura = (resultado_lista_matriculas[0][0]/resultado_lista_distinct_matriculas[0][0])
print(round(ratio_lectura, 2))
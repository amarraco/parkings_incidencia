# Conexion a la bbdd
import psycopg2 as p
from datetime import datetime, timedelta, date
from queries_mantenimiento_estadistica import total_dist_v_mc, total_dist_v_acceso_park, total_dist_v_hab_acceso_mc, total_dist_v_sancionables_hab_acceso_mc, total_dist_v_hab_acceso_park, total_v_sancionables_sin_acceso_park
from funciones_mantenimiento_estadistica import *

now = datetime.now()
start_date = start_date()
dias_habitualidad = resta_fecha(150)
accesos_habitualidad = resta_fecha(30)



print("Iniciando programa para el dia: " + str(start_date))

print("CONSULTA 1")
consulta_t_dist_v_mc = Conexion_mcval(total_dist_v_mc % start_date)
consulta_t_dist_v_mc = (consulta_t_dist_v_mc[0][0])

print("CONSULTA 2")
consulta_t_dist_v_acceso_park = Conexion_internet(total_dist_v_acceso_park % start_date)

print("CONSULTA 3")
consulta_t_dist_v_hab_acceso_mc = Conexion_mcval(total_dist_v_hab_acceso_mc % (dias_habitualidad, accesos_habitualidad, start_date))
print(consulta_t_dist_v_hab_acceso_mc)

print("CONSULTA 4")
consulta_t_dist_v_sancionables_hab_acceso_mc = Conexion_mcval(total_dist_v_sancionables_hab_acceso_mc % (dias_habitualidad, accesos_habitualidad, start_date))
print(consulta_t_dist_v_sancionables_hab_acceso_mc)

print("CONSULTA 5")
consulta_t_dist_v_hab_acceso_park = Conexion_internet(total_dist_v_hab_acceso_park % (dias_habitualidad, accesos_habitualidad, start_date))
print(consulta_t_dist_v_hab_acceso_park)

print("CONSULTA 6")
consulta_t_v_sancionables_sin_acceso_park = Conexion_mcval(total_v_sancionables_sin_acceso_park % (dias_habitualidad, accesos_habitualidad, start_date))

print("Programa finalizado")




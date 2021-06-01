import psycopg2 as p
import sys
from datetime import datetime
from datetime import timedelta
from Conexion_BBDD import *


def start_date():  # introduce fecha de inicio
    start_date = sys.argv[1]
    return start_date

def resta_fecha(numero):
     date = sys.argv[1]
     date = datetime.strptime(date, "%Y-%m-%d")  # convierte el str a objeto datetime
     numero = int(numero)
     resta_fecha = str(date - timedelta(days=numero))  # suma 1 dia
     return (resta_fecha[:10])  # devuelve la fecha fin sin la hora

def consultador(fecha, query):
    # Llama a la funcion Conexion_BBDD y hace una consulta
    consult = Conexion_internet(query % fecha)
    return (consult)

espacio = ""
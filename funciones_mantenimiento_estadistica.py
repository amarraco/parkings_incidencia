# Funciones Mantenimiento estadistica
import psycopg2 as p
import sys
from datetime import datetime, timedelta, date

def start_date():  # introduce fecha de inicio
    start_date = sys.argv[1]
    return start_date

# Resta a la fecha de hoy el parametro de entrada
def resta_fecha(numero):
    date = sys.argv[1]
    date = datetime.strptime(date, "%Y-%m-%d")  # convierte el str a objeto datetime
    numero = int(numero)
    resta_fecha = str(date - timedelta(days=numero))  # suma 1 dia
    return (resta_fecha[:10])  # devuelve la fecha fin sin la hora

#------------------------------------------------
# Conexion a la BBDD
query_conexion = "dbname=%s user=%s host=%s port =%s password =%s"

# Parametros bbdd mc_val
dbname='mc_val'
user='mc_val'
host='192.168.244.20'
port ='5432'
password ='mc_v4l'

def  Conexion_mcval(query):
    Conexion_mcval = p.connect("dbname='mc_val' user='mc_val' host='192.168.241.14' port ='5432' password ='G=b1$8}T'")
    Cursor_mcval = Conexion_mcval.cursor()
    Cursor_mcval.execute(query)
    Consulta_mcval = Cursor_mcval.fetchall()
    return Consulta_mcval
    Cursor_mcval.close()
    Conexion_mcval.close()

# Parametros bbdd mc_internet
dbname='mc_internet'
user='mc_internet'
host='192.168.241.14'
port ='5432'
password ='Dvj3gMO['

def  Conexion_internet(query):
    Conexion_internet = p.connect("dbname='mc_internet' user='mc_internet' host='192.168.241.14' port ='5432' password ='Dvj3gMO['")
    Cursor_internet = Conexion_internet.cursor()
    Cursor_internet.execute(query)
    Consulta_internet = Cursor_internet.fetchall()
    return Consulta_internet
    Cursor_internet.close()
    Conexion_internet.close()
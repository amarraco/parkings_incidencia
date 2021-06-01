# Funciones de conexion a la bbdd
import psycopg2 as p
import sys
from datetime import datetime
from datetime import timedelta
from datetime import date

def  Conexion_mcval(query):
    Conexion_mcval = p.connect("dbname='mc_val' user='mc_val' host='192.168.241.14' port ='5432' password ='G=b1$8}T'")
    Cursor_mcval = Conexion_mcval.cursor()
    Cursor_mcval.execute(query)
    Consulta_mcval = Cursor_mcval.fetchall()
    return Consulta_mcval
    Cursor_mcval.close()
    Conexion_mcval.close()

def  Conexion_internet(query):
    Conexion_internet = p.connect("dbname='mc_internet' user='mc_internet' host='192.168.241.14' port ='5432' password ='Dvj3gMO['")
    Cursor_internet = Conexion_internet.cursor()
    Cursor_internet.execute(query)
    Consulta_internet = Cursor_internet.fetchall()
    return Consulta_internet
    Cursor_internet.close()
    Conexion_internet.close()


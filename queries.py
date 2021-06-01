import psycopg2 as p
import sys
from datetime import datetime
from datetime import timedelta
from datetime import date

# Matriculas totales por dia
query_lista_matriculas = "select count(txt_matricula) from t_acceso_parking ap inner join t_usuario u on u.cod_usuario = ap.cod_usuario where date(ap.tmp_creacion ) = '%s' and ap.txt_ruta_foto_1 is not null and u.cod_colectivo in (43)"

# Matriculas unicas por dia
query_lista_distinct_matriculas = "select count(distinct txt_matricula) from t_acceso_parking ap inner join t_usuario u on u.cod_usuario = ap.cod_usuario where date(ap.tmp_creacion ) = '%s' and ap.txt_ruta_foto_1 is not null and u.cod_colectivo in (43)"

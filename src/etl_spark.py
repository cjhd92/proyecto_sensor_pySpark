import os
import sys
from pyspark.sql import SparkSession

from read_datos import read_sensor_data
from transformaciones import enrich_sensor_data,agregar_columnas_alerta,clasificar_nivel_alerta,agregar_promedio_movil
from load import load_particionado_parquet
# Forzar a Spark a usar el Python del entorno actual
os.environ["PYSPARK_PYTHON"] = sys.executable


# Crear sesión Spark
SpSession = SparkSession.builder \
            .appName('ETL_sensor-industrial') \
            .getOrCreate()










#Leer los datos del archivo
df = read_sensor_data(SpSession,"data/sensores.csv")
df = enrich_sensor_data(df)
df = agregar_columnas_alerta(df)
df = clasificar_nivel_alerta(df)
df = agregar_promedio_movil(df)
load_particionado_parquet(df)

df.show(truncate = False)





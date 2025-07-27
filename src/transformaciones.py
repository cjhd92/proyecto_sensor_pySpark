from pyspark.sql.functions import to_timestamp, col,hour, dayofmonth,when,avg
from pyspark.sql.window import Window


def enrich_sensor_data(df):
    df = df.withColumn("timestamp",to_timestamp("timestamp"))

    df = df.withColumn("hora",hour(col("timestamp")))
    df = df.withColumn("dia",dayofmonth(df.timestamp))


    return df

def agregar_columnas_alerta(df):
    """
    Agrega una columna booleana llamada 'alerta' si temperatura > 75 o presión > 200.
    """
    return df.withColumn(
        "alerta",
        ((col("temperature_c") > 75) | (col("pressure_bar") > 200)).cast("boolean")
    )

def clasificar_nivel_alerta(df):
    """
    Crea una columna categórica 'nivel_alerta':
    - 'ALTA' si temperatura > 90 o presión > 250
    - 'MEDIA' si temperatura entre 76-90 o presión entre 201-250
    - 'BAJA' si no hay condiciones críticas
    """
    
    df = df.withColumn(
        "nivel_alerta",
        when((col("temperature_c") > 90) | (col("pressure_bar") > 250), "ALTA")
        .when(((col("temperature_c") > 75) & (col("temperature_c") <= 90)) |
              ((col("pressure_bar") > 200) & (col("pressure_bar") <= 250)), "MEDIA")
        .otherwise("BAJA")
    )

    return df


def agregar_promedio_movil(df):
    """
    Agrega columna de promedio móvil de temperatura por sensor en una ventana de 3 registros.
    """
    window_spec = Window.partitionBy("sensor_id").orderBy("timestamp").rowsBetween(-1, 1)
    return df.withColumn(
        "temp_promedio_movil",
        avg(col("temperature_c")).over(window_spec)
    )
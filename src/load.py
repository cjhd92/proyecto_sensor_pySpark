def  load_particionado_parquet(df):
    df.write \
  .partitionBy("dia") \
  .mode("overwrite") \
  .option("header", True) \
  .csv("output/sensores_transformados_csv")

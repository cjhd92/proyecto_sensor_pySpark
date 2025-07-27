# 🔧 Proyecto de Procesamiento de Datos de Sensores Industriales con PySpark

Este proyecto simula un sistema de procesamiento de datos provenientes de sensores industriales (temperatura, presión, vibración) con PySpark. El objetivo es construir un pipeline ETL eficiente, modular y escalable para su análisis y detección de anomalías, utilizando herramientas reales empleadas en entornos industriales.

---

## 🧠 Objetivos del Proyecto

- Leer y transformar datos de sensores con PySpark.
- Aplicar lógica de negocio para generar alertas y niveles de criticidad.
- Calcular promedios móviles por sensor con ventanas temporales.
- Guardar los datos procesados en formato CSV particionado por día.
- Modularizar el proyecto siguiendo buenas prácticas (separación por fases).

---

## 🧱 Estructura del Proyecto

<img width="705" height="387" alt="image" src="https://github.com/user-attachments/assets/ddc93f6a-9675-40fb-91f0-6b3be21c3ae6" />

---

## ⚙️ Funcionalidades implementadas

- Limpieza y conversión de tipos de datos (`timestamp`, `float`).
- Extracción de variables temporales (hora, día).
- Generación de variable booleana `alerta` con condiciones de temperatura/presión.
- Clasificación de `nivel_alerta` como ALTA, MEDIA o BAJA.
- Cálculo de promedio móvil de temperatura por sensor (`window functions`).
- Escritura de resultados en CSV, con partición por día (`partitionBy`).

---

## 📌 Tecnologías utilizadas

- Python 3.10+
- PySpark
- CSV como formato de entrada
- CSV particionado como salida (simulación de Data Lake local)

---


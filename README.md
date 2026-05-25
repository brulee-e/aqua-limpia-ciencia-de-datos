# Análisis de desempeño de plantas de tratamiento de AquaLimpia S.A.

## Descripción del proyecto

Este proyecto corresponde al análisis exploratorio del desempeño operativo
y ambiental de las plantas de tratamiento de aguas residuales de AquaLimpia S.A.,
desarrollado como parte de la tarea de la semana 8 de la asignatura
Ciencia de Datos de IP IACC 2026.

El objetivo principal es apoyar la toma de decisiones de la empresa mediante
el análisis de los registros del último trimestre, identificando patrones de
incumplimiento normativo y diferencias de desempeño entre plantas.

---

## Objetivos

- Explorar y describir el comportamiento del dataset de aguas residuales.
- Calcular la eficiencia de remoción de DBO por planta.
- Identificar patrones de incumplimiento normativo.
- Generar archivos de salida diferenciados para el Área de Operaciones
  y el Área de Gestión Ambiental.
- Construir un dashboard exploratorio con visualizaciones complementarias.

---

## Estructura del proyecto

```
aqualimpia/
│
├── datos/
│   └── dataset_set_A_aguas_residuales.xlsx
│
├── scripts/
│   └── analisis_aqualimpia.py
│
├── salidas/
│   ├── reporte_operaciones.xlsx
│   └── reporte_gestion_ambiental.xlsx
│
└── dashboard/
    └── dashboard_aqualimpia.png
```

---

## Dataset

El dataset contiene 200 registros y 10 columnas con información operativa
y ambiental de tres plantas de tratamiento:

| Variable | Descripción |
|---|---|
| fecha_registro | Fecha del registro diario |
| planta | Planta de tratamiento (Centro, Norte y Sur) |
| caudal_entrada_m3_d | Caudal de entrada en m³/día |
| DBO_entrada_mg_L | Demanda biológica de oxígeno de entrada |
| SST_entrada_mg_L | Sólidos suspendidos totales de entrada |
| pH_entrada | pH del agua de entrada |
| energia_aeracion_kWh | Consumo de energía en aireación |
| lodos_generados_kg_d | Lodos generados en kg/día |
| DBO_salida_mg_L | DBO del efluente tratado |
| cumplimiento_norma | Cumplimiento normativo (1 = cumple, 0 = no cumple) |

---

## Librerías utilizadas

- `pandas` - carga y manipulación de datos
- `numpy` - cálculos numéricos
- `matplotlib` - visualizaciones y dashboard
- `openpyxl` - generación de archivos Excel

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Instalar las librerías necesarias:
   ```
   pip install pandas numpy matplotlib openpyxl
   ```
3. Colocar el dataset en la carpeta `datos/`
4. Ejecutar el script desde la carpeta raíz:
   ```
   python scripts/analisis_aqualimpia.py
   ```
5. Los archivos de salida se generarán en `salidas/` y `dashboard/`

---

## Principales resultados

- Solo el **22% de los registros** cumple con la normativa ambiental vigente.
- Las tres plantas presentan eficiencias de remoción de DBO similares.
  (entre 86% y 87%), lo que sugiere que el problema no es técnico.
- **Planta Norte** registra la mayor cantidad de incumplimientos (59 casos)
  y la tasa de cumplimiento más baja (17%).
- **Planta Sur** presenta la mejor tasa de cumplimiento (30%).
- No se observa correlación directa entre caudal de entrada y DBO de salida,
  lo que indica que otros factores operativos influyen en los incumplimientos.

---

## Autoría

Javiera Hormazábal H.  
Ingeniería en Informática - IP IACC 2026

import numpy as np
from scipy import stats
from joblib import dump, load

#calcula indicadores estadisticos de eficiencia de remoción de DBO
def calcular_indicadores_dbo(dbo_entrada, dbo_salida):
    dbo_entrada = np.array(dbo_entrada)
    dbo_salida = np.array(dbo_salida)

    eficiencia = ((dbo_entrada - dbo_salida) / dbo_entrada) *100

    promedio = np.mean(eficiencia)
    desviacion = np.std(eficiencia, ddof=1)

    #intervalo de confianza al 95% usando SciPy
    ic = stats.t.interval(
        0.95,
        df=len(eficiencia) - 1,
        loc=promedio,
        scale=stats.sem(eficiencia)
    )

    return {
        "eficiencia_promedio": round(float(promedio), 2),
        "desviacion_estandar": round(float(desviacion), 2),
        "ic95_inferior": round(float(ic[0]), 2),
        "ic95_superior": round(float(ic[1]), 2),
    }

#calcula estadísticas descriptivas del caudal de entrada.
def calcular_indicadores_caudal(caudal):
    caudal = np.array(caudal)

    return {
        "media": round(float(np.mean(caudal)), 2),
        "mediana": round(float(np.median(caudal)), 2),
        "desviacion_estandar": round(float(np.std(caudal, ddof=1)), 2),
        "minimo": round(float(np.min(caudal)), 2),
        "maximo": round(float(np.max(caudal)), 2),
    }

#calcula la tasa de incumplimiento normativo.
def tasa_incumplimiento(cumplimiento):
    cumplimiento = np.array(cumplimiento)
    total = len(cumplimiento)
    incumplimientos = int(np.sum(cumplimiento == 0))
    tasa = round((incumplimientos / total) * 100, 1)

    return {
        "total_registros": total,
        "incumplimientos": incumplimientos,
        "tasa_incumplimiento_pct": tasa,
    }

#guarda un diccionario de resultados usando Joblib para reutilizarlo en otros scripts sin recalcular.
def guardar_resultados(resultados, nombre_archivo):
    dump(resultados, nombre_archivo)
    print(f"Resultados guardados en {nombre_archivo}")

#carga resultados previamente guardados con Joblib.
def cargar_resultados(nombre_archivo):

    resultados = load(nombre_archivo)
    print(f"Resultados cargados desde {nombre_archivo}")
    return resultados

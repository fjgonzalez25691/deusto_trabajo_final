import csv, codecs, json, pandas as pd, os, locale, warnings
from Proyecto_final_archivos.funciones import crear_json

'''Leemos el csv y creamos el fichero json con la función crear_json. Posteriormente se crea una función para cada tipo
    de dato y se les llama desde el menú'''
try:
    warnings.filterwarnings("ignore")
    locale.setlocale(locale.LC_ALL, 'es_ES.utf8')


    # Si no existe el fichero Json se crea desde el csv
    if os.path.isfile('data.json') == False:
        crear_json()

    #creamos dataframe con pandas
    datos_json= pd.read_json('data.json')

    # Elegimos del dataFrame las columnas requeridas por el ejerciio
    datos = datos_json[["date", "province", "new_cases", "num_def", "num_hosp", "num_uci"]]

    # Vamos a realizar la agrupación que nos piden:
    datos["date"]=pd.to_datetime(datos["date"])
    datos["day_of_week"] = datos["date"].dt.weekday
    datos["day_name"] = datos["date"].dt.day_name()
    datos = datos.reindex(columns=['day_of_week', 'day_name', "date", "province", "new_cases", "num_def", "num_hosp", "num_uci"])

except Exception as ex:
    print(ex)

# Acumulados por provincia
def acum_prov(datos):  
    
    datos_cum_prov = datos.groupby("province")["new_cases",
                     "num_def", "num_hosp", "num_uci"].sum()
    print("             Acumlados totales por Provincia")
    print("========================================================")
    print(datos_cum_prov)
    return True

# Acumulados por día de la semana
def acum_day_week(datos):
    
    datos_cum_day_week = datos.groupby(["day_of_week", "day_name"])["new_cases",
                     "num_def", "num_hosp", "num_uci"].sum()

    print("              Acumlados totales por día de la semana")
    print("========================================================================")
    print(datos_cum_day_week)
    
    return True

# Acumulados por provincias y día de la semana
def acum_day_prov(datos):
            
    datos_day_cum_day_prov = datos.groupby(["day_of_week", "day_name", "province"])["new_cases",
                    "num_def", "num_hosp", "num_uci"].sum()

    print("              Acumlados totales provincia y día de la semana")
    print("========================================================================")
    
    print(datos_day_cum_day_prov)    
    return True

def menu_listados():
    try:
        opcion_listados = True
    
        while(opcion_listados):
            print("consulta de acumulados COVID-19")
            print("==================================")
        
            eleccion =int(input("""Elija una opción de visualización:
                1) Acumulados totales por provincia.
                2) Acumulados por día de la semana.
                3) Acumulados por provincia y día de la semana.
                4) Menú anterior \n"""))
            if eleccion == 1:
                acum_prov(datos)
            elif eleccion == 2:
                acum_day_week(datos)
            elif eleccion == 3:
                acum_day_prov(datos)
            elif eleccion == 4:
                opcion_listados = False
            else:
                print("Debe elegir una opción del menú")
    except ValueError as val_error:
        print("Debe de elegir una opción del menú")
        menu_listados()
    except Exception as ex:
        print(ex)


from .listados import datos
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


#Se define una función para mostrar el gráfico circular, pasando como parámetro el dato
def graf_prov_max_afec(num_dat):
        
    if num_dat == "num_def":
        pos_por = 1
        tit_enum = "Provincia con más defunciones:"
    elif num_dat == "new_cases":
        pos_por = 0
        tit_enum = "Porvincia con más casos nuevos:"
    elif num_dat == "num_hosp":
        pos_por = 2
        tit_enum = "Provincia con más hospitalizados:" 
    elif num_dat == "num_uci":
        pos_por = 3
        tit_enum= "Provincia con más enfermos en UCI:"    
    
    por = [0,0,0,0]
    por[pos_por] = 0.15
    datos_cum_prov = datos.groupby("province")["new_cases",
                        "num_def", "num_hosp", "num_uci"].sum()

    max_df = datos_cum_prov[num_dat].max()

    #nos devuelve la provincia con más  casos como "string"
    df_cum_max = datos_cum_prov[datos_cum_prov[num_dat]== max_df]
    prov_max_df = df_cum_max.index[0]
    
    datos_cum_prov = datos_cum_prov.reset_index()
    df2 = datos_cum_prov[datos_cum_prov["province"] == prov_max_df]

    df3 = df2.to_numpy().tolist()
   
   #modificamos los nombre de los ejes para su comprensión
    new_ind = df2.columns[1:5]
    new_ind_list = []
    for e in new_ind:
        new_ind_list.append(e)
    
    for i in range(len(new_ind_list)):
        if new_ind_list[i] == "new_cases":
            new_ind_list[i] = "Nuevos Casos"
        elif new_ind_list[i] == "num_def":
            new_ind_list[i] = "Nº Defunciones"
        elif new_ind_list[i] == "num_hosp":
            new_ind_list[i] = "Nº Hospitalizados"
        elif new_ind_list[i] == "num_uci":
            new_ind_list[i] = "Nº UCI"     
                                             
    new_data = df3[0][1:5]
   
   # Colores y función para los porcentajes y datos a mostrar en el gráfico circular
    colores = ['red','green','blue','yellow']
    
    def func (pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues)) 
        return "{:.1f}%\n({:d} casos)".format(pct, absolute)
    
    plt.figure(figsize=(12,7))
    plt.pie(new_data, labels=new_ind_list, autopct= lambda pct: func(pct,new_data), colors=colores, shadow=True, explode=por )  
    plt.legend(new_ind_list)
    plt.title(f'{tit_enum} {prov_max_df}', fontsize = 20, color='blue', fontweight='bold')
    plt.show()

def menu_graf_prov_max_afec():
    try:
        opcion_listados = True
    
        while(opcion_listados):
            print("Gráfico de provincia más afectada COVID-19")
            print("==================================")
        
            eleccion =int(input("""Elija una opción de visualización:
                1) Gráfico de provincia con más casos nuevos.
                2) Gráfico de provincia con más defunciones.
                3) Gráfico de provincia con hospitalizados.
                4) Gráfico de provincia con mas enfermos en UCI
                5) Menú anterior \n"""))
            if eleccion == 1:
                graf_prov_max_afec("new_cases")
            elif eleccion == 2:
                graf_prov_max_afec("num_def")
            elif eleccion == 3:
                graf_prov_max_afec("num_hosp")
            elif eleccion == 4:
                graf_prov_max_afec("num_uci")
            elif eleccion == 5:
                opcion_listados = False
            else:
                print("Debe elegir una opción del menú")
    except ValueError as val_error:
        print("Debe de elegir una opción del menú")
        menu_graf_prov_max_afec()
    except Exception as ex:
        print(ex)


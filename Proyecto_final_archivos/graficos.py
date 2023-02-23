from .listados import datos
import matplotlib.pyplot as plt
'''Se ha definido una función para cada uno de los gráficos y se las llama desde el menu principal'''

def graf_def():
    datos_cum_prov_def= datos.groupby("province")["num_def"].sum()

    datos_cum_prov_def.plot(figsize=(14,7), marker="x")
    plt.xlabel('Provincias', fontsize = 15, fontweight='bold')
    plt.ylabel('Número de defunciones', fontsize = 15, fontweight='bold')
    plt.gcf().subplots_adjust(bottom=0.30) 
    plt.title("Gráfica de defunciones", fontsize = 25, color='blue', fontweight='bold')
    plt.xticks(range(len(datos_cum_prov_def.index)),[i for i in datos_cum_prov_def.index], rotation=75)
    
    plt.grid(linestyle="dotted")
    plt.show()
    return True

def graf_casos():
    datos_cum_casos = datos.groupby("province")["new_cases"].sum()

    datos_cum_casos.plot(figsize=(14,7), marker="x")
    plt.xlabel('Provincias', fontsize = 15, fontweight='bold')
    plt.ylabel('Nuevos casos', fontsize = 15, fontweight='bold')
    plt.gcf().subplots_adjust(bottom=0.30) 
    plt.title("Gráfica de nuevos casos", fontsize = 25, color='blue', fontweight='bold')
    plt.xticks(range(len(datos_cum_casos.index)),[i for i in datos_cum_casos.index], rotation=75)
    
    plt.grid(linestyle="dotted")
    plt.show()
    return True

def graf_hospitalizados():
    datos_cum_hosp = datos.groupby("province")["num_hosp"].sum()

    datos_cum_hosp.plot(figsize=(14,7), marker="x")
    plt.xlabel('Provincias', fontsize = 15, fontweight='bold')
    plt.ylabel('Nuevas hospitalizaciones', fontsize = 15, fontweight='bold')
    plt.gcf().subplots_adjust(bottom=0.30) 
    plt.title("Gráfica de nuevas hospitalizaciones", fontsize = 25, color='blue', fontweight='bold')
    plt.xticks(range(len(datos_cum_hosp.index)),[i for i in datos_cum_hosp.index], rotation=75)
    
    plt.grid(linestyle="dotted")
    plt.show()
    return True

def graf_uci():
    datos_cum_uci = datos.groupby("province")["num_uci"].sum()

    datos_cum_uci.plot(figsize=(14,7), marker="x")
    plt.xlabel('Provincias', fontsize = 15, fontweight='bold')
    plt.ylabel('Nuevos ingresos en UCI', fontsize = 15, fontweight='bold')
    plt.gcf().subplots_adjust(bottom=0.30) 
    plt.title("Gráfica de nuevos ingresos en UCI", fontsize = 25, color='blue', fontweight='bold')
    plt.xticks(range(len(datos_cum_uci.index)),[i for i in datos_cum_uci.index], rotation=75)
    
    plt.grid(linestyle="dotted")
    plt.show()
    return True

    
def menu_graf():
    
    try:
        opcion_graficas = True
    
        while(opcion_graficas):
            print("           Gráficas COVID-19")
            print("====================================")
        
            eleccion =int(input("""Elija una gráfica a visualizar:
                1) Defunciones.
                2) Casos.
                3) Hospitalizaciones.
                4) UCI.
                5) Menú anterior \n"""))
            if eleccion == 1:
                graf_def()
            elif eleccion == 2:
                graf_casos()
            elif eleccion == 3:
                graf_hospitalizados()
            elif eleccion == 4:
                graf_uci()
            elif eleccion == 5:
                opcion_graficas = False
            else:
                print("Debe elegir una opción del menú")
                
    except ValueError as val_error:
        print("Debe de escoger un número")
        menu_graf()
    except Exception as ex:
        print(ex)
        



from Proyecto_final_archivos import listados, graficos, graf_prov_afc
'''He querido hacer un programa que integre los tres ejercicios. Desde este menú nos dirije a a listados.py para ver
    los informes de estadísticas, a graf_prov_afec.py que nos da las provincias con más casos y graficos.py para los gráficos 2D
    de los datos.'''

def estadisticas():
    listados.menu_listados()
    return True

def graficas():
    graficos.menu_graf()
    return True

def prov_mas_afec():
    graf_prov_afc.menu_graf_prov_max_afec()
    return True

def menu_principal():
    try:
        continuar = True
    
        while(continuar):
            print("MENU VISUALIZACION ESTADISTICAS COVID-19")
            print("==========================================")
        
            eleccion =int(input("""Elija una opción de visualización:
                1) Consulta de datos.
                2) Gráficas.
                3) Provincias más afectadas.
                4) Salir \n"""))
            if eleccion == 1:
                estadisticas()
            elif eleccion == 2:
                graficas()
            elif eleccion == 3:
                prov_mas_afec()
            elif eleccion == 4:
                continuar = False
            else:
                print("Debe elegir una opción del menú")
                
    except ValueError as val_error:
        print("Debe de eligir una opción del menú")
        menu_principal()
    except Exception as ex:
        print(ex)
        
menu_principal()
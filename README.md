# TRABAJO FINAL DE DEL CURSO DEUSTO

## Dashboard científico generado con Python y variables dinámicas
Se necesita desde un fichero .csv (accede al Campus online), extraer varios 
indicadores:
*Recuerda subir el fichero a la carpeta de trabajo, se eliminará 
automáticamente el fichero subido, pasado un tiempo.
* Ejercicio 1. 
    Almacena los datos del csv en un fichero txt en formato JSON, 
    agrupando los datos por día de la semana y por provincias, mostrar los 
    acumulado de defunciones, los nuevos casos de covid , hospitalizados y uci 
    (num_def,new_cases,num_hosp,num_uci).
    Utilizaremos el módulo csv para facilitar la lectura del fichero.
    import csv
    results = []
    with open('example.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
    results.append(row)
    print result
* Ejercicio 2.
     Realiza 4 gráficas de los datos almacenados en el fichero del 
    ejercicio anterior, realiza un menú con un bucle infinito para acceder a cada una 
    de las gráficas.
# Menú
int(input("""¿Qué gráfica quieres visualizar?
 1. Defunciones
 2. Casos
 3. Hospitalizados
 4. UCI
 5. Salir
 """))
* Ejercicio 3.
 Extrae del fichero generado en el ejercicio 1 que provincia contiene 
más defunciones, más casos, más hospitalizados y más en uci. Muestra el 
resultado en 4 gráficas de queso. Y realiza un menú como el ejercicio anterior. 
Después de mostrar la gráfica indica que provincia tiene el máximo de la 
variable a mostrar y cual la mínima
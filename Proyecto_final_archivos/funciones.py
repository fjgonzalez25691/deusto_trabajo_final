import json, codecs, csv

def crear_json():
    results = []

    with codecs.open("Proyecto_3.csv", 'r', encoding='utf-8', errors='ignore') as fichero:
        datos = csv.DictReader(fichero)
        for fila in datos:
            results.append(fila)

    with open('data.json', 'w') as file:
        json.dump(results, file, indent=4)

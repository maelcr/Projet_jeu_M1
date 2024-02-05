import csv
import os

def lire_map_depuis_doc():
    csv_file_path = os.path.join('src', 'map1.csv')

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        map = []
        for row in csv_reader:
            map.append(row[0].split(';'))

    return map
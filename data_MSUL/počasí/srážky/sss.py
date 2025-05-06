import csv

# Cesta k souboru
file_path = "srazky - kockov.csv"

with open(file_path, encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if len(row) >= 4:
            value = row[-4].replace('.', ',')  # tečku nahradíme čárkou
            print(value)  # třetí hodnota od konce

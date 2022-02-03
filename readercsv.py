#author : Mélanie Diligent

# On importe csv
import csv

# On déclare une fonction
def localisation():
# On déclare un tableau vide de données
    data = []

# On lit le fichier
    with open ("EtatDuParcTGO.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        for row in csvreader:
            # On rajoute chaque ligne lue dans le tableau data
            data.append(row)

    # Je peux maintenant travailler avec data (il dispose de toutes les données du csv)
    # On itère à travers le tableau afin d'obtenir ses données ligne par ligne
    numero_tc = 0
    for d in data:
        if numero_tc==d[1]:
            # Impression de la ligne 
            return(d[7])

# Signal pour le reader et lance le script
if __name__ == '__main__':
    localisation()

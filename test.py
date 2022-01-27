import csv

def searchByNumero():
    numero_tc=input('Entrez un numéro TC : ')
    csv_file=csv.reader(open('Etat_du_parc_TGO.csv','r'))

    for row in csv_file:
        if numero_tc==row[1]:
            print(row)

searchByNumero()
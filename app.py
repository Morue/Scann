from flask import (Flask, render_template, request, redirect,  url_for, flash)
import csv

from readercsv import localisation

app = Flask (__name__, template_folder='template')
app.secret_key = "1234"

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

# Lancement de la page d'accueil
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

# Lancement de la page de la localisation d'un container avec l'import de readercsv
@app.route("/result_localisation", methods = ["GET", "POST"])
# On déclare une fonction
def localisationTC():
    getLocalisation = localisation()
    flash('Le numéro TC ' + str(request.form['numeroTC']) + 'a pour localisation ')
    return render_template("localisation.html")

# Signal pour le reader et lance le script
if __name__ == '__main__':
    app.run(debug = True, port = 5001)
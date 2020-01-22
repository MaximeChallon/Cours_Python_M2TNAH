from flask import Flask

# app est l'appli web qui est une instance de flask (app est un objet, flask une classe)
app = Flask("Application")

# méthode route pour url/ qui correspondra à la fonction index: l'appli doit renvoyer le résultat de index sur la page de la racine
# route prend comme paramètre le chemin de ma page web: le décorateur dit pour ce chemin, exécute cette fonction (index())
@app.route("/")
def index():
    return "Hello world !"

app.run()

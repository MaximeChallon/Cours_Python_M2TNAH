from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from .constantes import SECRET_KEY

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

app = Flask(
    "Application",
    template_folder=templates,
    static_folder=statics
)
# On configure le secret
app.config['SECRET_KEY'] = SECRET_KEY
# On configure la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'
# On initie l'extension
db = SQLAlchemy(app)

# On met en place la gestion d'utilisateur-rice-s
login = LoginManager(app)

# ça se trouve ici car pour faire le @app.route, il faut que app soit définie; et comme PYhton exécute son code ligne
# après ligne, les routes doivent être mises ici, après la configuration de app, sinon on tourne dans le vide entre
# routes.py qui appelle ..app et app.py qui appelerait direct import routes, sans avoir configuré app avant : on évite
# l'import circulaire
from . import routes
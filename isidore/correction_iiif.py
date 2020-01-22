import csv
import requests


def iiif_csv(ark, nom_csv):

    colonnes = ["Numéro", "Nom de Page", "Lien image", "Largeur", "Longueur"]
    # Complétez avec la documentation'
    # LA REPONSE pour la requete HTTP GET sur l'adresse composee par l'ARK
    r = requests.get("http://gallica.bnf.fr/iiif/" + ark + "/manifest.json")
    # Permet de lire le contenu de la reponse json en tant que python
    # CAD de parser le body de la reponse http
    data = r.json()

    for x in data["metadata"]:
        print(x["label"] + " " + x["value"])

    with open(nom_csv, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(colonnes)
        numero = 0
        for canvases in data["sequences"][0]["canvases"]:
            numero += 1
            nom_de_page = canvases["label"]
            lien_image = canvases["images"][0]["resource"]["@id"]
            largeur = canvases["width"]
            longueur = canvases["height"]
            csv_writer.writerow([numero, nom_de_page, lien_image, largeur, longueur])


    return None

# Testez le code ici
iiif_csv("ark:/12148/btv1b84259980", "pages.csv")

@click.command()
@click.argument("ark", "nom_csv", type=str)
def iiif_csv(ark, nom_csv):
    """Commande qui affiche les métadonnées de l'objet décrit 
    sur Gallica en Json"""

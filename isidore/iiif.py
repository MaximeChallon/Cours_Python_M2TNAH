import click
import requests
import math
import csv

ISIDORE = "http://gallica.bnf.fr/iiif/ark:/12148/btv1b84259980/manifest.json"


def parser_reponse_gallica(data):
    """ Fait une recherche sur Gallica

    :param data: JSON Parsed Data
    :type q: dict
    :returns: Tuple (
        Nombre de Résultats,
        Nombre de Pages,
        Liste de résultat sous forme de dictionnaire {title, desc, author, date}
    )
    """
    # On récupère le nombre de résultats
    nb_items = len(data["sequences"][0]["canvases"])
    # On récupère le nombre de résultats par page
    items_per_page = 1
    # Le nombre total de pages est l'arrondi supérieur de la division nb_items / items_per_page
    total_page = math.ceil(nb_items / items_per_page)

    # On crée une liste vide dans laquelle on enregistrera les données
    items = []
    # Pour chaque réponse
    for item in data["sequences"][0]["canvases"]:
        # On ajoute à items un nouvel objet
        items.append({
            "uri": item["@id"],
            "title": item["label"],
            # dictionnaire.get(cle, valeur-par-defaut) : valeur-par-defaut est utilisée si clé n'est
            # pas présente
            "date": data["metadata"][6].get("valeur", "0000")
        })

    return nb_items, total_page, items


def cherche_gallica(q, full=False, page=1):
    """ Chercher sur isidore en faisant une requête

    :param q: Chaine de recherche
    :type q: str
    :param full: Recherche complète (itère sur toutes les pages)
    :type full: bool
    :param page: Page à récupérer
    :type page: int
    :returns: Tuple (
        Nombre de Résultats,
        Nombre de Pages,
        Liste de résultat sous forme de dictionnaire {uri, title, desc, author, date}
    )
    """

    # On exécute la requête
    params = {"output": "json", "q": q, "page": page}
    req = requests.get(ISIDORE, params=params)

    # On la parse
    nb_items, total_page, items = parser_reponse_gallica(req.json())

    if full:
        # On la parse
        nb_items, total_page, new_items= cherche_gallica(q=q, full=full, page=next_page)
        # On ajoute chacune des valeurs d'items à total_items
        items.extend(new_items)

    return nb_items, total_page, items

@click.command()
@click.argument("query", type=str)
def run(query):
    """ Exécute une recherche sur Isidore.science en utilisant [QUERY]
    """
    nb_items, total_page, items = cherche_gallica(query)
    print("Nombre de résultats : {}".format(nb_items))
    print("Nombre de résultats affichés : {}".format(len(items)))
    for item in items:
        print("{}".format(item["title"]))

# Si ce fichier est le fichier exécuté directement par python
# Alors on exécute la commande
if __name__ == "__main__":
    run()
# modules/memoire_long_terme.py

import json
import os

FICHIER_MEMOIRE = "memoire.json"


# chargement du fichier json
def charger_memoire():
    if not os.path.exists(FICHIER_MEMOIRE):
        return {"discussions": [], "preferences": {}}

    with open(FICHIER_MEMOIRE, "r", encoding="utf-8") as f:
        return json.load(f)  # on lit le json


def sauvegarder_memoire(memoire):
    with open(FICHIER_MEMOIRE, "w", encoding="utf-8") as f:
        json.dump(memoire, f, indent=4)


def ajouter_discussion(user, reponse):
    memoire = charger_memoire()
    memoire["discussions"].append({"user": user, "ia": reponse})
    sauvegarder_memoire(memoire)


def ajouter_préference(cle, valeur):
    memoire = charger_memoire()
    memoire["preferences"][cle] = valeur
    sauvegarder_memoire(memoire)


def get_preference(cle):
    memoire = charger_memoire()

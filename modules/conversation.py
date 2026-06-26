from datetime import datetime
import random

# importation des mes modules personnalisés
from modules.system_control import executer_commande
from modules.memoire_long_terme import ajouter_discussion, ajouter_préference
from modules.intentions import intentions
from modules.reponses import reponses
from modules.meteo import obtenir_meteo_leger
from modules.engine import ruphia_ultra_engine


def score_phrase(message, mots_cles):
    """Calcule le score de correspondance entre le message et les mots-clés."""
    score = 0
    message_mots = message.lower().split()

    for mot in message_mots:
        for mot_cle in mots_cles:
            # On vérifie si le mot clé est contenu dans le mot ou vice-versa
            if mot_cle in mot or mot in mot_cle:
                score += 1

    # TRÈS IMPORTANT : Le return doit être HORS des boucles for
    return score


def detecter_intention(message):
    """Détermine l'intention de l'utilisateur basée sur le meilleur score."""
    meilleur_score = 0
    meilleure_intention = "inconnu"

    for intention, mots in intentions.items():
        score = score_phrase(
            message, mots
        )  # importation de la fonction score_phrase,celle de la correspondance

        if score > meilleur_score:
            meilleur_score = score
            meilleure_intention = intention

    # Le return doit être ici, après avoir analysé TOUTES les intentions
    return meilleure_intention


def discuter(message):
    """Moteur principal de discussion et d'exécution."""

    # 2. Détection de ce que l'utilisateur veut (Intention)
    intention = detecter_intention(message)

    # 3. Traitement des Calculs (Intention "calcul")
    # Ajout d'une sécurité : si l'IA voit un signe mathématique, elle calcule d'office
    if intention == "calcul":
        return ruphia_ultra_engine(message)
    # c'est ici que la magie s'opera avec le module executer_commande
    if any(
        mot in message.lower()
        for mot in ["ouvre", "ferme", "crée", "found file", "delete"]
    ):
        return executer_commande(message)

    # 4. Heure et Date
    if intention == "heure":
        return f"Il est actuellement {datetime.now().strftime('%H:%M:%S')}."

    if intention == "date":
        return f"Nous sommes le {datetime.now().strftime('%d/%m/%Y')}."

    # 5. Météo
    if "METEO" in message.upper() or "MÉTÉO" in message.upper():
        return obtenir_meteo_leger(message)

    # 6. Réponses classiques (depuis ton dictionnaire)
    reponse = reponses.get(intention, reponses.get("inconnu"))

    # Si plusieurs réponses possibles, on en choisit une au hasard
    if isinstance(reponse, list):
        reponse = random.choice(reponse)

    # 7. Gestion de la mémoire et des préférences
    ajouter_discussion(message, reponse)
    analyser_prefernces(message)

    return reponse


def analyser_prefernces(message):
    """Extrait des informations du message pour la mémoire à long terme."""
    msg = message.lower()

    if "je m'appelle" in msg:
        nom = message.split("je m'appelle")[-1].strip()
        ajouter_préference("nom_user", nom)

    if "j'aime" in msg:
        passion = message.split("j'aime")[-1].strip()
        ajouter_préference("aime", passion)

import os  # importation du module os le module systeme
from modules.intentions import (
    intentions,
)  # importation de ma bibliotheque intentions que j'ai créé dans mon fichier "intention.py"

# Dictionnaire des applications et leurs commandes d'exécution
APPLICATIONS = {
    "cmd": "cmd",
    "visual studio code": "code",
    "vscode": "code",
    "calculatrice": "calc",
    "bloc-notes": "notepad",
    "whatsapp": "whatsapp",
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "chrome": "chrome",
    "opera": "opera",
    "explorateur": "explorer",
    "powershell": "powershell",
}

# Dictionnaire des processus et leurs noms d'exécution
PROCESSUS = {
    "chrome": "chrome.exe",
    "opera": "opera.exe",
    "bloc-notes": "notepad.exe",
    "calculatrice": "CalculatorApp.exe",
    "vscode": "Code.exe",
    "visual studio code": "Code.exe",
    "explorateur": "explorer.exe",
    "powershell": "powershell.exe",
    "cmd": "cmd.exe",
}


def executer_commande(message):
    """
    Exécute une commande en fonction du message reçu.


        message (str): Le message reçu.

    Returns:
        str: Une réponse appropriée en fonction de la commande exécutée.
    """
    message = message.lower()

    if "ouvre" in message or "lense" in message:
        # Recherche de l'application correspondante dans le dictionnaire APPLICATIONS
        for app, command in APPLICATIONS.items():
            if app in message:
                # Exécution de la commande pour ouvrir l'application
                os.system(f'start "" "{command}"')
                return f"Maitre Ruphin {app.capitalize()} est ouvert sur votre serveur"

        return "Seigneur Ruphin, Cette application n'est pas dans ma BIBLIOTHEQUE"

    if "ferme" in message or "close" in message:
        # Recherche du processus correspondant dans le dictionnaire PROCESSUS
        for app, exe in PROCESSUS.items():
            if app in message:
                # Exécution de la commande pour fermer le processus
                os.system(f"taskkill /IM {exe} /F")
                return f" Commande executé!seigneur Ruphin l'application {app.capitalize()} est fermé."

        return "Impossible de fermer cette application."

    if "ouvre le fichier" in message or "open file" in message:

        try:
            # Récupération du chemin du fichier à ouvrir à partir du message
            chemin = message.split("ouvre le fichier")[
                1
            ].strip()  # on coupe le message en deux parties dont on recupre le plus importante
            # si le chemin est correct

            if os.path.exists(chemin):
                if os.path.isfile(chemin):

                    # Exécution de la commande pour ouvrir le fichier
                    os.system(f'start "" "{chemin}"')
                    return f"Fichier ouvert : {os.path.basename(chemin)}"

                elif os.path.isdir(chemin):
                    # Exécution de la commande pour ouvrir le dossier desiré ou pour autre usage
                    # on recupere le chemin et on lense le dossier dans explorer
                    os.system(f'start "" "{chemin}"')
                    return "C'est un dossier, je l'ai ouvert dans votre explorer."
                else:
                    return f"l'adresse {chemin} est introuvable ou n'est pas reconnu sur votre serveur."
        except IndexError:
            return "Veuillez préciser le chemin exact du fichier"
        except Exception as e:
            return f"Erreur système : {str(e)}"
            """ ici ruphia gere la creation de mes dossiers et fichiers et les efacer"""
    if "found file" in message or "found folder" in message:
        try:
            chemin = message.split("found folder")[
                1
            ].stript()  # on coupe le message en deux parties et on recupere le chemin
            os.mkdir(chemin)  # la touche de geni qui va  créer le  dossier qu'on désire
            return f"Dossier {chemin} est créé sur votre projet"

        # on recupere l'erreur telqu'il soit
        except Exception as e:
            return f"Maitre Ruphin l'erreur systeme est: {str(e)}"

    # la structure qui gere les suppressions des fichiers bat dangereux et autres fichiers indésirables
    if "delete" in message or "supprimer" in message:
        command = message.split("delete file")[1].stript()
        try:
            os.remove(
                command
            )  # le coup de géni qui va effacer n'importe quel fichier indésirable
            return (
                f"Sa supremassie le fichier {command} est  placé dans votre corbeille"
            )
        # si le fichier n'existe pas unitile de l'effacer car il n'est pas la

        except FileNotFoundError:
            return f" le fichier {command} n'existe pas"

            # on envoi ca dans la console de mon serveur 'Ruphia'
            print(
                f"serveur en marche, le fichier {command} est en plaine connexion avec ruphia"
            )

    return None

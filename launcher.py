import subprocess  # C'est mon chef d'orchestre pour lancer mes serveurs
import getpass  # Pour plus tard : cacher le mot de passe quand on le tape
import hashlib  # Mon outil de cryptographie pour sécuriser les accès
import json  # Pour lire ma base de données des serveurs
import os  # Pour gérer les variables d'environnement de mon PC
import sys  # Pour pouvoir fermer le programme proprement

# Ici, je charge ma base de données qui contient mes serveurs et mes hashs
with open("login.json", "r") as f:
    servers = json.load(f)


# Voici ma fonction de sécurité : elle transforme un texte en empreinte SHA-256.
# C'est ce qui fait de Ruphin os  un vrai monstre de sécurité !
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def main():

    print("------ Welcome to the Ruphin OS ---------------")

    # 1. Je demande l'identité de celui qui veut entrer
    user = input("Please, specify your identity before starting: ").lower()

    # Ensuite, je demande quel serveur l'utilisateur veut démarrer
    server_name = input(
        f"Welcome King Ruphin! Enter the name of the server to launch: "
    ).lower()

    # Je vérifie tout de suite si le serveur existe dans mon fichier JSON
    if server_name not in servers:
        print("Error: Unknown server. Access denied.")
        sys.exit()  # On arrête tout si le serveur n'existe pas

    # 2. On passe à l'étape du mot de passe
    pwd = input(f"{user}, please enter the password for '{server_name}': ")

    # La ligne magique : je hache ce que l'utilisateur tape et je compare
    # avec le hash que j'ai stocké secrètement dans mon login.json
    if hash_password(pwd) == servers[server_name]["password_hash"]:
        print(f"Authentication successful. Starting {server_name}...")

        # 3. Je crée un badge d'accès (Token) pour que le serveur sache
        # qu'il a bien été lancé par mon launcher officiel
        my_env = os.environ.copy()
        my_env["AUTH_TOKEN"] = "GRANTED"

        # Je lance le serveur en lui donnant mon badge de sécurité
        subprocess.Popen(servers[server_name]["command"], env=my_env)
    else:
        # Si le hash ne correspond pas, personne ne passe !
        print("Error: Incorrect password. Access denied.")


# Je lance le programme principal
if __name__ == "__main__":
    main()

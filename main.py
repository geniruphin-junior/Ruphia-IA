from modules.conversation import discuter
from modules.conversation import discuter
from modules.memoire import memoire
from voice import parler

name = input("mets ton identité pour débuter :")


def discut():

    print("=== Ruphia est en ligne 🤖 ===")

    while True:

        if name == "ruphin":

            user = input(f"noble:")
            reponse = discuter(user)
            print("Ruphia :", reponse)
            parler(reponse)
        else:
            user = input(f"{name}: ")
            reponse = discuter(user)
            print("Ruphia :", reponse)

        if user.lower() in ["quit", "exit"]:
            print("Ruphia : À bientôt 👋", name)
            break


if __name__ == "__main__":
    discut()

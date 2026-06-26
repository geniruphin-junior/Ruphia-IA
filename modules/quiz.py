import random
import sys

# Liste des questions du quiz pour Ruphia
quiz_data = {
    "Qui est le créateur de Python ?": "Guido van Rossum",
    "Que signifie HTML ?": "HyperText Markup Language",
    "Quel est le symbole chimique de l'or ?": "Au",
    "En quelle année est né Internet (ARPANET) ?": "1969",
    "Quelle planète est surnommée la planète rouge ?": "Mars",
    "Quel langage est utilisé pour le style d'une page web ?": "le css",
    "qui est le fondateur de ruphia": "c'est ruphin",
}


def lancer_quiz_ruphia():
    print("Ruphia : Bonjour ! Prêt pour un petit quiz scientifique ?")
    score = 0
    # On mélange les questions pour ne pas avoir toujours le même ordre
    questions = list(quiz_data.items())
    random.shuffle(questions)
    for question, reponse_correcte in questions:
        print(f"\nRuphia : {question}")
        reponse_utilisateur = input("Ta réponse : ").strip()
        # Vérification (on ignore la casse pour être plus souple)
        if reponse_utilisateur.lower() == reponse_correcte.lower():
            print("Ruphia : Correct ! Bravo.")
            score += 1
        elif reponse_utilisateur.lower() in ["exit", "arrete"]:
            sys.exit()
        else:
            print(f"Ruphia : Dommage... La bonne réponse était : {reponse_correcte}")

    print(f"\nRuphia : Quiz terminé ! Ton score final est de {score}/{len(quiz_data)}.")

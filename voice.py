import pyttsx3  # la bibliotheque de la voix
import threading  # qui va resonner en arriere plan
import time  # time comme son nom l'indique
import re


def _filtre_sublimato_dieu(texte):
    """
    TRANSFORMATION QUANTIQUE DU TEXTE :
    Prépare le texte pour une élocution que l'oreille humaine
    ne peut pas classer comme artificielle.
    """
    if not texte:
        return ""

    # 1. Nettoyage absolu des scories visuelles (Emojis/Markdown)
    # Seuls les caractères de fréquence humaine passent
    texte = "".join(
        c
        for c in texte
        if c
        in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789àâéèêëîïôûùçÀÂÉÈÊËÎÏÔÛÙÇ ,.:;!?'-"
    )

    # 2. DICTIONNAIRE DE PRÉCISION CHIRURGICALE
    # On modifie l'orthographe pour FORCER la bonne prononciation
    dictionnaire = {
        "IA": "IA.",
        "Ruphia": "Ru-phi-a,",  # La virgule ici change l'intonation descendante
        "Ruphin": "Ru-phin.",  # Le point force une fin de mot noble
        "V4.0": "Version quatre, point zéro",
        "OS": "O. S.",
        "Bonjour": "Bonjour...",  # Pause de reconnaissance
    }
    for mot, rep in dictionnaire.items():
        texte = re.sub(rf"\b{mot}\b", rep, texte)

    # 3. LE SECRET DU DIEU VOCAL : LA PONCTUATION INVISIBLE
    # On injecte des silences mathématiques
    texte = texte.replace(".", " . . . ")  # Pause de réflexion profonde
    texte = texte.replace(",", ", ")  # Respiration courte
    texte = texte.replace("?", " ? .")  # Intonation de curiosité

    return texte


def _process_divine_vocal(texte):
    try:
        engine = pyttsx3.init("sapi5")

        # --- RÉGLAGES QUE LES INGÉNIEURS N'OSENT PAS TOUCHER ---

        # La vitesse "Alpha" : 190.
        # C'est la fréquence de résonance du calme absolu.
        engine.setProperty("rate", 190)
        engine.setProperty("volume", 2.0)

        voices = engine.getProperty("voices")
        # Sélection de la voix la plus riche en harmoniques
        target_voice = None
        for voice in voices:
            if "JULIE" in voice.name.upper() or "HORTENSE" in voice.name.upper():
                target_voice = voice.id
                break

        if target_voice:
            engine.setProperty("voice", target_voice)

        # Préparation du texte purifié et rythmé
        texte_final = _filtre_sublimato_dieu(texte)

        if texte_final.strip():
            # Déclenchement de la parole
            engine.say(texte_final)
            engine.runAndWait()

        engine.stop()
        del engine

    except Exception as e:
        print(f"🔱 Échec du moteur : {e}")


def parler(texte):
    """
    Lancement en mode Archange : asynchrone et invisible.
    """
    if texte:
        # On lance dans un thread daemon pour libérer tes 4.0 Go de RAM
        threading.Thread(
            target=_process_divine_vocal, args=(texte,), daemon=True
        ).start()


# --- DÉMONSTRATION DU SOMMET ---
if __name__ == "__main__":
    parler("Bonjour Ruphin. Je suis Ruphia. Mon code est pur, ma voix est éternelle.")

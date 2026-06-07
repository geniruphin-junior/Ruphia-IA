import os
import sys
import threading
import time
import psutil
import platform
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    Response,
    stream_with_context,
)

# Import des  mes modules personalisés
from modules.conversation import discuter
from voice import parler

# Sécurité Launcher
if os.environ.get("AUTH_TOKEN") != "GRANTED":
    print("Accès non autorisé.")
    sys.exit(1)

app = Flask(__name__)

historique_calculs = []


@app.route("/")
def home():
    return render_template("windows.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        raw_msg = data.get("message", "").strip()

        if not raw_msg:
            return jsonify({"reply": "Message vide..."}), 400

        # --- 1. LOGIQUE RUPHIN SHELL (Réponse JSON Directe) ---
        if raw_msg.startswith("/"):
            clean_cmd = raw_msg.replace("//", "/").lstrip("/")
            parts = clean_cmd.split()
            if not parts:
                return jsonify({"reply": "..."})

            cmd = parts[0].lower()

            if cmd == "info":
                ram = psutil.virtual_memory()
                res = f"[SYSTÈME] RAM: {ram.percent}% | OS: {platform.system()}"
                return jsonify({"reply": res})

            elif cmd == "last":
                derniers = (
                    "\n".join(historique_calculs[-5:])
                    if historique_calculs
                    else "Aucun."
                )
                return jsonify({"reply": f"[HISTORIQUE]\n{derniers}"})

            elif cmd == "ls":
                fichiers = "\n".join(os.listdir("F:/projet ia/projet_ruphia")[:10])
                return jsonify({"reply": f"[FICHIERS]\n{fichiers}"})

            return jsonify({"reply": f"Commande '{cmd}' inconnue."})

        # --- 2. LOGIQUE CHAT IA (RÉTABLISSEMENT DU STYLE ET DE LA VOIX) ---
        reponse_ia = discuter(raw_msg)

        # Archivage
        if "=" in reponse_ia:
            historique_calculs.append(f"{raw_msg} = {reponse_ia[:20]}")

        # LANCEMENT DE LA VOIX (Thread séparé)
        threading.Thread(target=parler, args=(reponse_ia,)).start()

        # GÉNÉRATEUR POUR L'ÉCRITURE MOT PAR MOT
        def generate():
            for mot in reponse_ia.split():
                yield mot + " "
                time.sleep(0.07)  # Ton rythme original

        # On renvoie un flux TEXTE (mimetype text/plain) pour le streaming
        return Response(stream_with_context(generate()), mimetype="text/plain")

    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

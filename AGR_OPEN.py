from flask import Flask, render_template, request, jsonify
from modules.conversation import discuter

app = Flask(__name__)


# ======================
# Charger interface
# ======================
@app.route("/")
def home():
    return render_template("windows.html")


# ======================
# CHAT IA
# ======================
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data.get("message")

    # 🔥 appel direct du cerveau agr
    reponse_ia = discuter(user_message)

    return jsonify({
        "reply": reponse_ia
    })


# ======================
# Lancement serveur
# ======================
if __name__ == "__main__":
    app.run(debug=True)


import urllib.request
import json
import ssl 

def obtenir_meteo_leger(ville="Goma"):
    contexte_ssl = ssl._create_unverified_context()
    
    # AJOUT DU SLASH ICI : wttr.in/{ville}
    url = f"https://wttr.in{ville}?format=j1"
   
    try:
        requete = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(requete, context=contexte_ssl, timeout=15) as response:
            data = json.loads(response.read().decode())
            
            # current_condition est une LISTE, on prend l'index [0]
            current = data['current_condition'][0]
            temp = current['temp_C']
            
            # weatherDesc est aussi une LISTE dans le JSON de wttr.in
            desc = current['weatherDesc'][0]['value']
            
            return f"🌤️ MÉTÉO RUPHIA : À {ville}, il fait {temp}°C ({desc})."
            
    except Exception:
        # PLAN B (Version simplifiée si le JSON est trop lourd pour la RAM)
        try:
            url_simple = f"https://wttr.in{ville}?format=3"
            with urllib.request.urlopen(url_simple, context=contexte_ssl, timeout=10) as res:
                return f"🌤️ MÉTÉO RUPHIA : {res.read().decode().strip()}"
        except:
            return "❌ Ruphia : Serveur indisponible. Vérifie ton Wi-Fi."

if __name__ == "__main__":
    print(obtenir_meteo_leger("Goma"))

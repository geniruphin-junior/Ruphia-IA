let dotsInterval;

// Fonction pour démarrer l'animation des points
function startTypingAnimation() {
    const dots = document.getElementById("dots");
    if (!dots) return;  // Si l'élément "dots" n'existe pas, on ne fait rien

    let count = 0;

    dotsInterval = setInterval(() => {
        count = (count + 1) % 4;
        dots.textContent = ".".repeat(count);  // Affiche 1, 2 ou 3 points
    }, 500);  // Chaque 500ms, changer le nombre de points
}



// Fonction pour arrêter l'animation des points
function stopTypingAnimation() {
    clearInterval(dotsInterval);  // Arrêter l'intervalle d'animation

    const dots = document.getElementById("dots");
    if (dots) dots.textContent = "";  // Effacer les points affichés
}

// Gestion du formulaire d'envoi de message
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const chatBox = document.getElementById('chatBox');

chatForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const messageText = userInput.value.trim();
    if (messageText === "") return;

    // 1. Afficher le message utilisateur
    const userDiv = document.createElement('div');
    userDiv.className = 'msg user-msg';
    userDiv.textContent = messageText;
    chatBox.appendChild(userDiv);

    // 2. Préparer l'indicateur (le remettre en bas et l'allumer)
    const typing = document.getElementById('typing-indicator');
    chatBox.appendChild(typing); 
    typing.style.display = 'block';
    
    userInput.value = "";
    startTypingAnimation();
    chatBox.scrollTop = chatBox.scrollHeight;

    
        // 3. Appel au serveur (Version STABLE)
    fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: messageText }) // Ici, PAS de "/" devant
})
.then(response => {
    if (!response.ok) throw new Error('Erreur réseau');
    
    stopTypingAnimation();
    typing.style.display = 'none';

    // Création de la bulle IA vide
    const aiDiv = document.createElement('div');
    aiDiv.className = 'msg ai-msg';
    chatBox.appendChild(aiDiv);

    // --- LECTURE DU FLUX (STREAMING) ---
    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    function readStream() {
        return reader.read().then(({ done, value }) => {
            if (done) return;

            // Décodage du texte brut envoyé par Flask (yield)
            let chunk = decoder.decode(value, { stream: true });

            // NETTOYAGE : Si par erreur du JSON arrive, on enlève les scories
            if (chunk.includes('{"reply":')) {
                try {
                    const data = JSON.parse(chunk);
                    chunk = data.reply;
                } catch(e) {
                    chunk = chunk.replace('{"reply": "', '').replace('"}', '');
                }
            }
            
            // Ajout du texte mot par mot
            aiDiv.textContent += chunk; 

            // Scroll automatique
            chatBox.scrollTop = chatBox.scrollHeight;

            return readStream();
        });
    }
    return readStream();
})
.catch(error => {
    stopTypingAnimation();
    typing.style.display = 'none';
    const errorDiv = document.createElement('div');
    errorDiv.className = 'msg ai-msg';
    errorDiv.style.color = '#ff0055';
    errorDiv.textContent = "Système déconnecté. Relancez le noyau.";
    chatBox.appendChild(errorDiv);
});
})
// Fonction pour ajouter un message à la chat-area
function addMessage(text, className) {
    const div = document.createElement('div');
    div.classList.add('msg', className);
    div.textContent = text;
    chatBox.appendChild(div);

    // Scroll automatique vers le bas
    chatBox.scrollTop = chatBox.scrollHeight;
}
function showTab(tabId) {
    // 1. Cacher toutes les sections
    document.querySelectorAll('.tab-content').forEach(content => {
        content.style.display = 'none';
    });

   


    // 2. Afficher la section choisie avec le bon mode
    const target = document.getElementById(tabId);
    if (tabId === 'chat-section' || tabId === 'shell-section') {
        target.style.display = 'flex'; // Le chat a besoin de flex pour l'input
    } else {
        target.style.display = 'block'; // Projets et Settings sont en block
    }

    // 3. Style de la barre latérale
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    event.currentTarget.classList.add('active');

    // 4. Titre dynamique
    const titles = {
        'chat-section': 'Ruphia chat-bot',
        'shell-section':'terminal core',
        'projects-section': 'Workspace Explorer',
        'settings-section': 'Configuration Ruphia'
    };
    document.getElementById('tab-title').textContent = titles[tabId];
}
// AFFICHAGE DE L'HEURE
function showtime() {
    const now = new Date();

    let heures = now.getHours().toString().padStart(2, '0');
    let minutes = now.getMinutes().toString().padStart(2, '0');
    let secondes = now.getSeconds().toString().padStart(2, '0');

    const heureComplete = `${heures}:${minutes}:${secondes}`;

    document.getElementById("clock").textContent = heureComplete;
}


// LE JEU D'IMAGES DE MON BODY----------------------------------------------
function changerFond() {
    let heure = new Date().getHours();
    let body = document.getElementById("page-body");
     if (heure >= 6 && heure < 18) {
        body.style.backgroundImage = "url('/static/e.png')";
    } else {
        body.style.backgroundImage = "url('/static/chatgpt.png')";
    }
}
changerFond();
setInterval(changerFond, 60000);

// NOUVEAU CHAT----------------------------------------------------------------------

function nouveauChat(){
    location.reload();
}


// JEU DE COULEURS JOUR ET NUIT----------------------------------------------------
function adapterAmbianceSite() {
    const heure = new Date().getHours();
    const corpsPage = document.body;
    // On vérifie l'heure (Nuit entre 18h et 6h du matin)
    if (heure >= 18 || heure < 6) {
        // --- MODE NUIT : NOIR ---
        corpsPage.style.backgroundColor ="#000000"; // Un beau noir
        corpsPage.style.transition = "background-color 2s ease"; // Animation douce
        console.log("Ambiance Nuit activée");
        confirm('veux tu vraiment ruphia à changer en mode night ?');
    } else {
        // --- MODE JOUR : BLEU ---
        corpsPage.style.backgroundColor =  "#001a33"; // blue de nuit pur
        corpsPage.style.transition = "background-color 2s ease";
        console.log("Ambiance Jour activée");
        
    }

}
// FONCTION CANEVAS COMPLETE-------------------------------------------------
window.onload = adapterAmbianceSite;
const canvas = document.getElementById('fond-ia');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
// Création de petits points "neurones"
const neurones = [];
for (let i = 0; i < 30; i++) { // Pas trop pour tes 4Go de RAM
  neurones.push({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    vx: (Math.random() - 0.5) * 0.5,
    vy: (Math.random() - 0.5) * 0.5
  });
}
function dessiner() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = 'rgba(0, 242, 254, 0.4)'; // Couleur des points
  ctx.strokeStyle = 'rgba(0, 242, 254, 0.1)'; // Couleur des lignes
  for (let n1 of neurones) {
    // Déplacement des points
    n1.x += n1.vx; n1.y += n1.vy;
    // Rebond sur les bords
    if (n1.x < 0 || n1.x > canvas.width) n1.vx *= -1;
    if (n1.y < 0 || n1.y > canvas.height) n1.vy *= -1;
    // Dessin du point
    ctx.beginPath();
    ctx.arc(n1.x, n1.y, 2, 0, Math.random()*1);
    ctx.fill();
    // Dessin des connexions
    for (let n2 of neurones) {
      const dist = Math.sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2);
      if (dist < 100) { // Si proches, on trace une ligne
        ctx.beginPath();
        ctx.moveTo(n1.x, n1.y);
        ctx.lineTo(n2.x, n2.y);
        ctx.stroke();
      }
    }
  }
  requestAnimationFrame(dessiner);
}
dessiner();

// LE BOUTON EFFACER LES LOGS
function purgeChat() {
    // 1. Demander une confirmation (pour éviter les erreurs)
    if (confirm("⚠️ Voulez-vous vraiment réinitialiser le noyau et effacer tous les logs ?")) {
        
        // 2. Nettoyer l'interface de Chat
        const chatArea = document.querySelector('#chat-section .chat-area');
        if (chatArea) {
            chatArea.innerHTML = `
                <div class="msg ai-msg">Système réinitialisé. Historique effacé.</div>
            `;
        }

        // 3. Nettoyer le Ruphin Shell (si tu veux aussi vider le terminal)
        const shellOutput = document.getElementById('shell-output');
        if (shellOutput) {
            shellOutput.innerHTML = `<p style="color: #ff0055;">[ALERTE] LOGS PURGÉS PAR L'UTILISATEUR.</p>`;
        }

        // 4. Envoyer l'ordre au serveur Flask pour vider la mémoire
        fetch('/clear_memory', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            console.log("Mémoire serveur vidée");
            // Optionnel : petit message de succès
            alert("Base de données nettoyée.");
        })
        .catch(err => console.error("Erreur lors de la purge :", err));
    }

 }
 // --- Mode Jour/Nuit ---
function toggleTheme() {
    document.body.classList.toggle("night-mode");
    // Feedback console
    if (document.body.classList.contains("night-mode")) {
        console.log("Mode Nuit activé 🌌");
    } else {
        console.log("Mode Jour activé 🌞");
    }
}

// --- Sauvegarde des logs ---
let logsEnabled = true;
function toggleLogs() {
    logsEnabled = !logsEnabled;
    console.log("Sauvegarde des logs : " + (logsEnabled ? "activée 💾" : "désactivée ❌"));
    // Ici tu peux ajouter la logique pour activer/désactiver la sauvegarde réelle
}

// --- Langue FR/EN ---
let langFR = true;
function toggleLang() {
    langFR = !langFR;
    console.log("Langue actuelle : " + (langFR ? "Français 🇫🇷" : "Anglais 🇬🇧"));
    // Ici tu peux ajouter la logique pour changer les textes affichés
}





// RUPHIA SHEL-------------------------------------------------/////////
function executerShell() {
    const input = document.getElementById('shell-input');
    const output = document.getElementById('shell-output');
    const cmd = input.value.trim();

    if (!cmd) return;
    output.innerHTML += `<div style="color: #fff; margin-top: 10px;">> ${cmd}</div>`;

    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: "/" + cmd }) 
    })
    .then(async response => {
        const contentType = response.headers.get("content-type");
        
        // Si le serveur renvoie du JSON (pour les commandes Shell)
        if (contentType && contentType.includes("application/json")) {
            const data = await response.json();
            return data.reply;
        } 
        // Si le serveur renvoie du texte brut (si l'IA répond par erreur)
        else {
            return await response.text();
        }
    })
    .then(resultat => {
        output.innerHTML += `<div style="color: #00ff7f; white-space: pre-wrap;">${resultat}</div>`;
        output.scrollTop = output.scrollHeight;
    })
    .catch(err => {
        console.error(err);
        output.innerHTML += `<div style="color: #ff4444;">[ERREUR] Interprétation noyau échouée.</div>`;
    });

    input.value = "";
}
/**
 * CONFIGURATION DU MOTEUR DE RECONNAISSANCE
 * On vérifie si le navigateur supporte l'API (Chrome/Edge utilisent webkitSpeechRecognition)
 */
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

// On crée une instance de l'intelligence auditive de Ruphia
const recognition = new SpeechRecognition();

// Paramètres de langue et de comportement
recognition.lang = 'fr-FR';          // Définit la langue sur le français
recognition.interimResults = false;  // Attend la fin de la phrase avant d'afficher (plus propre)
recognition.maxAlternatives = 1;     // Ne propose qu'une seule réponse (la plus probable)

/**
 * FONCTION DE DÉCLENCHEMENT (Liée au bouton HTML)
 * Cette fonction s'exécute quand tu cliques sur l'icône du micro
 */
function toggleEcoute() {
    const micIcon = document.getElementById('mic-icon');
    const inputField = document.getElementById('userInput');

    try {
        // Démarre l'enregistrement audio via le navigateur
        recognition.start();
        demarrerVisualiseur();
        
        // --- Feedback Visuel (Style Ruphin OS) ---
        // On change la couleur de l'icône en rouge pour indiquer que Ruphia "écoute"
        micIcon.style.color = "#ff4444";
        micIcon.style.filter = "drop-shadow(0 0 10px #ff4444)";
        
        // On change le texte d'aide dans la barre de saisie
        inputField.placeholder = "Ruphia vous écoute...";
        
        console.log("Système d'écoute activé.");
    } catch (error) {
        // Evite de faire planter le script si on clique deux fois trop vite
        console.warn("L'écoute est déjà en cours ou a été bloquée.");
    }
}

/**
 * GESTION DU RÉSULTAT
 * Cet événement se déclenche quand le navigateur a fini de transformer le son en texte
 */
recognition.onresult = (event) => {
    // On extrait la chaîne de caractères (le texte) du résultat
    const texteCapture = event.results[0][0].transcript;
    
    // On sélectionne ton champ de texte
    const inputField = document.getElementById('userInput');
    
    // On injecte le texte capté directement dans la barre de saisie
    inputField.value = texteCapture;
    
    console.log("Texte reçu : " + texteCapture);
    
    /** 
     * ASTUCE : Si tu veux que Ruphia réponde direct sans cliquer sur la flèche, 
     * décommente la ligne ci-dessous :
     */
    // document.querySelector('.send-btn').click();
};

/**
 * FIN DE L'ÉCOUTE
 * Se déclenche quand le micro s'éteint (soit par erreur, soit parce que tu as fini de parler)
 */
recognition.onresult = (event) => {
    // 1. On récupère le texte
    const texteCapture = event.results[0][0].transcript;
    
    // 2. On l'affiche dans l'input
    const inputField = document.getElementById('userInput');
    inputField.value = texteCapture;
    
    console.log("Texte reçu : " + texteCapture);

   // On lance le chrono de 1 seconde avant d'envoyer
    setTimeout(() => {
        console.log("Envoi automatique...");
        document.querySelector('.send-btn').click();
    }, 1000); 
};

/**
 * GESTION DES ERREURS (Sécurité)
 */
recognition.onerror = (event) => {
    console.error("Erreur de reconnaissance : " + event.error);
    // Si l'utilisateur refuse le micro, on peut l'alerter ici
};

function afficherHeure() {
    const clock = document.getElementById("clock");
    const now = new Date();
    clock.textContent = now.toLocaleTimeString();
}
setInterval(afficherHeure, 1000);
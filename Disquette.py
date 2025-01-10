# Instructions pour configurer l'envoi automatique de messages sur WhatsApp

# 1. Connexion préalable à WhatsApp Web
#    Assurez-vous d'être connecté à WhatsApp Web via votre navigateur avant d'exécuter ce script.
#    Cela garantit que le message sera envoyé correctement.

# 2. Ajout d'une exception pour le fichier .bat dans l'antivirus
#    Si votre antivirus bloque le fichier .bat :
#    - Accédez aux paramètres de votre antivirus.
#    - Ajoutez une exception ou une exclusion pour le fichier .bat dans les paramètres de sécurité.
#      Exemple pour AVG :
#      - Allez dans "Menu" > "Paramètres" > "Exceptions".
#      - Ajoutez le chemin du fichier .bat.

# 3. Configuration du planificateur de tâches (Windows Task Scheduler)
#    - Ouvrez le planificateur de tâches sur Windows.
#    - Créez une nouvelle tâche.
#    - Configurez-la pour qu'elle s'exécute uniquement si vous êtes connecté à la session.
#    - Activez l'option "Exécuter la tâche dès que possible si une exécution planifiée est manquée".
#    - Assurez-vous de définir correctement l'heure et la fréquence d'exécution.
#######################################################################################################

import pywhatkit
import datetime
import time
import socket
import random

# Fonction pour vérifier la connexion Internet
def check_internet():
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except OSError:
        return False

# Attendre jusqu'à ce que le Wi-Fi soit connecté
def wait_for_internet():
    print("Vérification de la connexion Internet...")
    while not check_internet():
        print("Pas de connexion Internet. Nouvelle tentative dans 5 secondes...")
        time.sleep(5)
    print("Connexion Internet établie.")

# Liste des contacts et leurs préférences
contacts = [
    {"nom": "Ginette", "numéro": "+37062822336"},
    # Ajoutez d'autres contacts ici
]

# Liste des phrases de drague
pickup_lines = [
    # Classiques intemporelles
    "Tu crois au coup de foudre ⚡, ou je dois repasser près de toi ? 😏",
    "Excuse-moi, tu as un briquet ? Parce que tu viens d’allumer un feu en moi. 🔥❤",
    "T’as une carte ? Parce que je viens de me perdre dans tes yeux. 🗺✨",
    "Si être magnifique était un crime 🚔, tu serais coupable à perpétuité. 🥵❤",
    "Excuse-moi, mais est-ce que tu es un rayon de soleil ? Parce que tu éclaires ma vie. 🌞✨",

    # Compliments directs
    "Ton sourire pourrait illuminer la pièce la plus sombre. 😊❤",
    "Quand je te regarde, j’oublie tous mes problèmes. 🌍❤",
    "Tu es comme un diamant 💎 : rare, précieuse, et magnifique. ✨",
    "Tu es comme une rose 🌹 : belle, délicate, et unique.",
    "Ton rire est une mélodie 🎵 que je pourrais écouter pour toujours. ❤✨",

    # Humour léger et décalé
    "Es-tu un Wi-Fi gratuit ? Parce que je suis automatiquement connecté à toi. 📶❤",
    "Tu es comme un bug dans mon système : tu fais tout planter dans ma tête. 💻❤",
    "Es-tu un prêt bancaire ? Parce que tu as tout mon intérêt. 💸❤",
    "Si tu étais un mot de passe, tu serais impossible à oublier. 🔒✨",
    "Es-tu une pizza ? Parce que je ne veux pas te partager. 🍕🥰",

    # Poésie et douceur
    "Tu es comme une étoile filante 🌠 : rare, magique, et impossible à ignorer. ✨",
    "Si j’avais une fleur 🌸 pour chaque pensée que j’ai de toi, je vivrais dans un jardin infini. ❤",
    "Ton sourire est comme un lever de soleil 🌅 : il réchauffe et illumine ma journée.",
    "Ton regard est comme un océan 🌊 : profond et captivant.",
    "Quand je te regarde, je découvre un trésor plus précieux que l’or. 🏆❤",

    # Références modernes
    "Tu es comme une série Netflix : je pourrais te regarder pendant des heures. 🎥❤",
    "Si tu étais une application, tu serais celle qui rend ma vie meilleure. 📱❤",
    "Es-tu un compte Insta ? Parce que je veux te suivre partout. 📸✨",
    "Tu es comme une mise à jour : tu rends tout meilleur autour de toi. 💾❤",
    "Es-tu un QR code ? Parce que je veux te scanner et découvrir tous tes secrets. 📲✨",

    # Drôles et ludiques
    "Es-tu un croissant 🥐 ? Parce que tu es irrésistible.",
    "Tu es comme un chocolat chaud : réconfortante, douce, et totalement addictive. ☕❤",
    "Es-tu un ticket de loterie ? Parce que je sens que tu es mon gros lot. 🎟❤",
    "Si la beauté était un marathon, tu serais la ligne d’arrivée. 🏁❤",
    "Es-tu un miroir ? Parce que je me vois passer ma vie avec toi. 🪞❤",

    # Audacieuses et originales
    "Excuse-moi, tu es magique ? Parce que tu rends tout autour de toi plus beau. ✨❤",
    "Es-tu un coffre au trésor ? Parce que je ne trouve que de l’or dans ton sourire. 💎❤",
    "Tu es comme un feu d’artifice 🎆 : spectaculaire et impossible à oublier.",
    "Es-tu un dictionnaire ? Parce que tu donnes un sens à ma vie. 📖❤",
    "Quand je suis avec toi, c’est comme si le monde s’arrêtait pour admirer ta beauté. 🌍❤",

    # Métaphores modernes
    "Tu es comme un algorithme parfait : tu optimises tout autour de toi. 💻❤",
    "Tu es comme une story Instagram : je ne veux jamais que tu disparaisses. 📱❤",
    "Es-tu une chanson ? Parce que tu es bloquée dans ma tête. 🎶❤",
    "Es-tu un soleil ? Parce que même à distance, je ressens ta chaleur. 🌞❤",
    "Quand je te vois, c’est comme si je regardais mon écran préféré. 🎥❤",

    # Compliments sincères
    "Je pensais que les anges 👼 vivaient au ciel… jusqu’à ce que je te voie.",
    "Si j’étais un peintre 🎨, je n’aurais jamais assez de couleurs pour te décrire.",
    "Ton sourire, c’est comme une porte ouverte sur le bonheur. 🚪❤",
    "Tu es la raison pour laquelle je crois encore aux contes de fées. 🧚‍♀✨",
    "Quand je suis près de toi, mon cœur bat comme un tambour. ❤🥁",

    # Douce poésie
    "Si je pouvais décrire ta beauté en un mot, ce serait : indescriptible. ❤✨",
    "Tu es comme un coucher de soleil 🌅 : beau, apaisant, et captivant.",
    "Quand je te vois, c’est comme si toutes les étoiles 🌌 se rassemblaient dans ton sourire.",
    "Si les fleurs 🌸 parlaient, elles diraient que tu es leur modèle.",
    "Ton énergie est comme une batterie externe : tu recharges mon cœur. 🔋❤",

    # Phrases finales fortes
    "Tu es comme une flamme : impossible à ignorer, et je ne veux pas m’éloigner. 🔥❤",
    "Es-tu une rose ? Parce que même avec tes épines, je te trouve parfaite. 🌹✨",
    "Quand je te regarde, c’est comme si j’avais trouvé ce que j’avais toujours cherché. ❤✨",
    "Si je pouvais écrire un livre 📖, il parlerait uniquement de toi.",
    "Ton sourire est la seule lumière dont j’ai besoin dans ma vie. 🌞❤",
]

# Vérifier la connexion Internet
wait_for_internet()

# Parcourir tous les contacts pour envoyer un message
for contact in contacts:
    print(f"Préparation du message pour {contact['nom']}...")
    
    # Choisir une phrase de drague aléatoire
    message = random.choice(pickup_lines)
    print(f"Message choisi : {message}")

    # Planifier l’envoi du message immédiatement
    heure = datetime.datetime.now().hour
    minute = (datetime.datetime.now().minute + 2) % 60
    if minute == 0:
        heure = (heure + 1) % 24

    print(f"Envoi prévu à {heure:02}:{minute:02} pour {contact['nom']}.")

    # Envoyer le message via WhatsApp
    try:
        pywhatkit.sendwhatmsg(contact['numéro'], message, heure, minute)
        print(f"Message envoyé à {contact['nom']} !")
    except Exception as e:
        print(f"Erreur lors de l'envoi à {contact['nom']}: {e}")

print("Tous les messages ont été traités.")

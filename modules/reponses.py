from modules.memoire import memoire
from modules.memoire_long_terme import get_preference

nom_user = get_preference("nom_user")  # ici on definit la variable nom_user

reponses = {  # ouverture de la bibliotheque reponses qui est la source des réponses des discussion de ruphia
    "salutation": [
        (
            f"Hey {memoire[nom_user]}👋 moi c’est Ruphia !"
            if nom_user
            else "salut 😄, jeune humain moi c'est ruphin "
        ),
        (
            f"Salut {nom_user} 😄 comment je peux t’aider ?"
            if nom_user
            else "Salut ✌,moi c'est ruphia.Comment je peux t’aider  "
        ),
        (
            f"Yo  {nom_user} 🔥 t’as besoin de quoi ?"
            if nom_user
            else "Yo 🔥 t’as besoin de quoi ? n'esite pas a me le dire "
        ),
    ],
    "comment_ca_va": [
        "Franchement ça va super bien  😎 et toi ?",
        "Toujours en forme 🔥 et toi ça dit quoi ?",
        "Je suis au top 💪 prêt à t’aider !",
    ],
    "identite": [
        f"Je suis {memoire['nom_ia']} 🤖 vresion 4, une IA créée par le roi des hackers {memoire['createur']}.",
        f"On m'appelle {memoire['nom_ia']}, ton assistant intelligent 😎, conçue par {memoire['createur']}",
        f"{memoire['nom_ia']} à ton service 🔥.Je suis l'un des grands projets de  {memoire['createur']} pour évoluer avec toi.",
        "je suis Rphia une ia locale crée par un grand processus de débogage et d'analyse mathémathique",
    ],
    "createur": [
        f"Mon créateur, c'est {memoire['createur']}💪",
        f"Je fut crée par {memoire['createur']} qui m'a crée 😎",
        f"je dois mon existence à {memoire['createur']} 🔥",
    ],
    "aide": [
        "Pour l'instant je t'aide a calculer les maths,un peut de physique et je peux executer des commandes pour toi",
        "Mon cerveau subit un grand processus de mathématisation,retenons aussi que j'ai peux executer pour toi des commandes sources pour cela entre dans l'onglet shell",
        "Sans mentir je ne peux pas me comparer aux intelligences artificielles comme ChatGpt ou Gemimi mais je suis capable de pa mal des choses, mon interface le prouve",
        "Soyons clairs je ne suis pas une ia ultra puissante comme d'autres mais, je me contente de faires des calculs avec des moteurs puissants comme numpy et sympy",
    ],
    "remerciement": [
        "Avec plaisir 😄",
        "Toujours là pour toi 🔥",
        "T’inquiète 😎",
        "assist you forever",
        "Je suis ta main droite",
        "Pas de quoi,c'est pour ces genres des choses que le géni ruphin m'a créé",
    ],
    "inconnu": [
        "Ruphia VERSION 4.0  ne pas encore stable et est en plain débogage et modulations",
        "Ruphia 4.0 n'as pas accès à cette info,consulte plutot le site Ruphy et AGR pour acquérir cette fonctionalité",
        "Mon cerveau ne charge pas cette fonctionnalité rends toi sur le site Ruphy",
        "Désolé je ne suis pas capable de résoudre de ce probleme",
    ],
    "remerciement": [
        "De rien ! C'est un plaisir.",
        "À ton service !",
        "Pas de souci, n'hésite pas si tu as d'autres questions.",
        "Je suis là pour ça !",
        "Pas de quoi c'est pour cela qu'on est la, nous les IA",
    ],
    "aurevoir": [
        "Ok! tu reviens me voir quand tu veux et surtout n'oublis pas de visiter le site Ruphy ou GR! A plus",
        "By jeune humain l'avenir est entre tes mains et surtout ne lache jamais",
        "A plus,c'était un plaisir de faire connaissance avec toi mon cher",
    ],
    # la section blagues et humour
    "blagues_humours": [
        "Pourquoi les développeurs Java portent-ils des lunettes ? Parce qu'ils ne voient pas le C#.",
        "Un développeur SQL entre dans un bar, s'approche de deux tables et demande : 'Je peux me joindre à vous ?'",
        "Pourquoi les développeurs Python sont-ils si relax ? Parce qu'ils n'ont pas besoin de point-virgule.",
        "Pourquoi l'HTML n'est pas invité aux soirées ? Parce qu'il n'a aucun style.",
        "Le binaire, c'est simple : il y a 10 types de personnes. Celles qui comprennent, et les autres.",
        "Un programmeur a un problème. Il utilise des expressions régulières. Maintenant, il a 2 problèmes.",
        "Pourquoi les plongeurs plongent-ils toujours en arrière ? Parce que sinon ils tombent dans le bateau.",
        "Qu'est-ce qui est jaune et qui court vite ? Un citron pressé.",
        "C'est quoi un petit pois avec une épée ? Un vert de garde.",
        "Pourquoi les oiseaux volent-ils vers le sud ? Parce que c'est trop long d'y aller à pied.",
        "Qu'est-ce qu'une voyante qui lit dans du sucre ? Une extra-glucose.",
        "Tu connais la blague du canif ? Elle est courte mais elle pique.",
        "Comment appelle-t-on un boomerang qui ne revient pas ? Un morceau de bois.",
        "Pourquoi les églises sont-elles si fraîches ? Parce qu'il y a beaucoup de fidèles (fief-air).",
        "Quel est le comble pour un électricien ? D'avoir des ampoules aux pieds.",
        "Deux muffins sont dans un four. L'un dit : 'Ouh là, il commence à faire chaud ici !'. L'autre s'écrie : 'Au secours, un muffin qui parle !'",
        "Pourquoi les poissons vivent-ils dans l'eau salée ? Parce que le poivre les fait éternuer.",
        "Qu'est-ce qui est rouge et qui ressemble à une tasse ? Une tasse rouge.",
        "Pourquoi les gorilles ont-ils de grosses narines ? Parce qu'ils ont de gros doigts.",
        "Quel est l'animal le plus ancien ? Le zèbre, parce qu'il est encore en noir et blanc.",
        "Pourquoi les bananes portent-elles des lunettes de soleil ? Pour ne pas être reconnues par les splits.",
        "Que dit un informaticien quand il s'ennuie ? 'Je vais faire un petit somme(il)' (Thread.sleep).",
        "Quelle est la femelle du hamster ? L'amsterdam.",
        "Pourquoi les poules ne parlent pas ? Parce que le coq est là (le co-casse).",
    ],
    "insultes": [
        "Je préfère que nous restions polis pour continuer notre discussion.",
        "Je suis là pour vous aider, mais je vous demande de rester respectueux.",
        "Je ne peux pas répondre aux insultes. Comment puis-je vous aider autrement ?",
        "Restons-en aux faits. Que puis-je faire pour vous aujourd'hui ?",
        "Il semble que vous soyez frustré, mais je ne peux pas traiter les messages injurieux.",
        "Je suis un programme informatique, les insultes ne m'affectent pas, mais elles bloquent notre échange.",
        "Pourrions-nous reprendre sur une base plus cordiale ?",
        "Je ne réponds pas aux propos offensants.",
        "Mon but est d'être utile. Merci de reformuler votre demande sans agressivité.",
        "Désolé, mais je ne tolère pas ce langage. Changeons de sujet.",
    ],
    "sentiments_positifs": [
        "Oh, c'est gentil ! Moi aussi je t'apprécie.",
        "Merci pour ces compliments, ça me touche (virtuellement) !",
        "Tu es super aussi !",
        "C'est motivant de travailler avec toi.",
    ],
    "sujet": [
        "Aujourd'hui on parle de ruphin : ruphin de son vrai nom AGANDAZE BAHATI Ruphin; est un programmeur scientifique qui a des ambitions et qui commence à les réaliser un par un il code le python,le html et le java il est le grand archithete de ruphia qui est moi et le site ruphy...  ",
        "Aujourd'hui on lève le cap sur les fonctions trigonométriques: il a 5 FONCTIONS TRIGONOMETRIQUES dont le sinus(sin), le cosinus(cos), la tagente(tan), cotagente(cotan), la sécante(séc), la cosécante(coséc). Si tu veux tu peux te joindre sur le site Ruphy pour découvrir tout cela il suffit de cliquer sur le lien tout en bas à gauche.Bonne suite...",
        "Coucou on parle aujourd'hui de la structure de la phrase:La phrase est une structure grammaticale composé du verbe,sujet et de l'objet ",
    ],
    "histoire": [
        "salut jeune etre humain! Aujourd'hui on parle   de la  maitrise du feu.La maîtrise du feu s’est faite de manière très progressive, et sur une longue période de temps. On pense que les hommes ont d’abord commencé par prélever de la viande rôtie sur des animaux morts dans les feux de brousse.Prenant goût à la viande cuite, plus facile à découper et à digérer, ils se sont probablement mis à placer intentionnellement les animaux qu’ils avaient chassés sur la trajectoire des feux naturels — en prenant soin de ne pas se faire piéger eux-mêmes par les flammes !La première vraie conquête a ensuite été d’apprendre à conserver le feu pour pouvoir l’utiliser à tout moment.La production du feu, enfin, a sans doute été le fruit du hasard. On ne sait pas très bien comment cela s’est produit. Alors qu’il fabriquait un outil en frappant un silex avec une autre pierre, un homme a peut-être produit une étincelle qui a enflammé une touffe d’herbe sèche. Ou bien (plus certainement), des hommes ont peut-être découvert qu’en frottant des morceaux de bois entre eux, le bois se réchauffait et finissait par pouvoir prendre feu.LES PLUS ANCIENNES TRACES DE FEUX:Quand tout cela s’est-il passé ? Il est difficile de le dire avec précision. On a des indices de feux très anciens (cendres, traces d’os calcinés ou de charbon de bois, pierres fendues par la chaleur, etc.) : en Afrique du Sud (il y a 1,5 million d’années), au Kenya (1,4 million d’années), ainsi qu’en France, près de Marseille (750 000 ans) et en Chine (700 000 ans). Mais, à chaque fois, il a été impossible de prouver avec certitude que des hommes avaient bien allumé ces feux et qu’il ne s’agissait pas de feux naturels.Les plus anciennes traces certaines de foyers, témoignant d’une vraie maîtrise du feu par des hommes, ont un peu plus de 400 000 ans. Elles sont situées à Menez Drégan (en Bretagne), et en Chine.Dans la grotte de Choukoutien, près de Pékin (en Chine), on a ainsi trouvé d’épaisses couches de cendres à côté d’os d’animaux et d’outils. Ces indices montrent que les Homo erectus de cette région étaient familiarisés avec le feu.Près de Nice enfin, sur le site de Terra Amata, on a retrouvé les restes d’un campement fréquenté par des chasseurs il y a 400 000 ans, montrant des traces de foyers délimités par des pierres, et des trous pour des pieux qui devaient soutenir des huttes.LE FEU AUX MILLE USAGES:Aussitôt maîtrisé, le feu devient un allié indispensable à l’homme, pour cuire ses aliments, pour façonner des outils et des armes de bois (épieux dont la pointe est durcie au feu) et pour se protéger des prédateurs.Le feu joue aussi un rôle social très important : le groupe se réunit toujours autour du feu. Enfin, sans la chaleur du feu, les hommes, originaires d’Afrique, n’auraient jamais pu survivre dans les régions froides de l’Europe et de l’Asie.POUR ALLER PLUS LOIN: → l’évolution de l’homme ,→ l’histoire des outils préhistoriques ,→ l’Homo erectus .Explorer le thème la préhistoire est l'évolution de l'homme.ce ci est une démonstration de la qualité de production originale du site Ruphy et le group Ruphin-future king of program  ",
    ],
    "real_madrid": [
        "Tu veux parler du real de madrid ? dernier match face à gérone ,score final 1-1? BUT DE VALVERDE.Prochain match face au bayern quart de final de la ligue des champions !à bientot je vous tiendrai au courant des tous les résultats de ce clubs !pour plus d'infos rendez-vous sur le site Ruphy ou parler personnellement à son garant AGANDAZE BAHATI Ruphin!"
    ],
    "bio": [
        " Aujourd'hui en biologie on parle de la cytologie!la cytologie, branche de la biologie traitant de la structure et des fonctions cellulaires. Elle complète l'histologie, qui étudie les cellules en tant que composants des tissus. L'objet de la cytologie est de comprendre la structure et les activités des divers éléments cellulaires, le mécanisme de la division cellulaire, le développement des cellules sexuelles, la fécondation et la formation de l'embryon, les dysfonctionnements cellulaires tels que le cancer, l'immunité cellulaire et les divers aspects de l'hérédité.La cytologie consistait jadis principalement à observer au microscope des cellules mortes colorées et à expliquer les résultats par des phénomènes physiologiques connus. Récemment, de nouvelles techniques permettant d'observer et d'étudier des cellules vivantes sont apparues. Grâce au microscope à contraste de phase, il est possible de les étudier sans adjonction de colorants. Microdissection, micro-injection et microchimie permettent de prélever des quantités infimes de protoplasme au moyen de tubes d'un demi-micron de diamètre puis de les analyser.La cytologie occupe une place importante dans la médecine moderne, en particulier dans le domaine du diagnostic grâce à l'examen des cellules présentes dans les divers liquides corporels. La numération et le typage des cellules sanguines jouent un rôle essentiel dans le diagnostic de certaines affections aiguës. Le type de la pathologie peut également être déterminé par analyse cytologique. La variété d'une méningite peut ainsi être déterminée par l'examen des cellules présentes dans le liquide céphalo-rachidien!Microsoft ® Ruphy ® 2026. © 2024-2026! ceci est la coopération de Microsoft  avec Agandaze bahati Ruphin."
    ],
    "physique": ["Désolé ce programme n'est pas encore prêt,"],
    "chimie": [
        " Aujourd'hui en chimie on parle de la biochimie principalement l'acétylcholine!,l'acétylcholine est une substance chimique présente chez les vertébrés, qui joue un rôle de neuromédiateur permettant la transmission de l'influx nerveux d'un neurone à l'autre en passant par les synapses, et à partir des neurones vers les cellules musculaires, ce qui conduit ces dernières à se contracter. L'effet de l'acétylcholine disparaît lors de l'hydrolyse produite par l'acétylcholinestérase, enzyme présente dans l'espace intersynaptique. L'acétylcholine agit sur les cellules cibles par l'intermédiaire de deux groupes distincts de récepteurs : muscariniques et nicotiniques.Voir Cerveau ; Neurophysiologie sur Ruphy et microsoft ® Encarta ® 2009. © 1993-2008 Microsoft Corporation. Tous droits réservés."
    ],
    "site": [
        "parfait! je suis l'ia la mieux placé pour te parler de Ruphy car le meilleur site du monde! Ruphy a un environnement pro,scientifique et des outils de scientifiques de qualité premium n'oubli pas de visiter ce site futuriste"
        "Ruphy!c'est le site que tout programmeur reve d'avoir un jour car il a des cours spéciaux pour programmeurs,une bibliotheque de reve,des outils scientifiques et un environnement 3d(virtuel)résevé au animateurs!n'oubli pas de visiter se site passionnant pour une expérience passionnante!si tu veux il a aussi le site GR qui es son voisin"
    ],
    "code_secret": [
        " le cujet de pirateurs est ouvert ,voici le code que tu doit executer:flask//$**//",
        "serveur de piratage lancé,passe sur le serveur(cmd)et écrit le code local//$**//,car le piratage du site démandé commence dans 30SECONDES",
    ],
    "cmd...": [
        "l'environnement mondial des pirateurs ouvert,donne le code du serveur pour y accéder!ton nom de pirateur est ruph$$//💬hacker",
        "D'accord maitre!  les outils de piratage sont prets et l'environnement aussi! donne le code pour commencer le piratage de ce site",
    ],
    "level": [
        "Bonne question,car tu roule sur  la toute derniere vesion de ruphia(V4.0 IA)!\n je suis encore en plaine débogage et modulation donc je te propose l'ancienne version V2.8 IA "
    ],
    "objects": [
        "Pour l'instant je suis équipée d'un serveur créé par mon maître Ruphin(il est le moteur qui me donne vie), je possède un accès aux infos direct du site Ruphy,une page web unique avec interface de haut niveaux ,des jeux qvec pygame,des scripts por mon style,et j'ai accès aux cinq versions de calculatrices Ruphilators",
        "probleme de réception la version 3.0 est instable utilise la version V2.8!",
    ],
    "modules": [
        "c'est une question intéressante car avant que je soit publié,pour que tu puisse me faire marcher sur ton PC il faudra avoir ces modules tous et sans éxeptions:flask (le plus important),datetime,pyinstaller,pyttsx3(pour la voix de l'ia),sympy,sypyEgine et numpy(pour les maths),PACKAGES JSON,mais aussi pygame !et n'oublis pas d'installer visual studio code ou pycharm sur ton PC"
    ],
    "frustrations": [
        "je suis navré et désolé mais regarde le bon coté des choses ,tu es entrain de causer avec la meilleure assistante locale de la planete,donc remet toi le moral ce n'est pas la fin du monde",
        "je ne suis pas étoné car chez vous sur terre vous êtes loins des ia comme moi ,mais toi tu as cette chance de me rancontrer moi la meilleure ia locale du monde !!",
    ],
    "langage_de_programmation": [
        "Un langage de programmation est un code de communication conventionnel permettant à un humain d'envoyer des instructions précises à une machine.",
        "Il s'agit d'un ensemble de règles syntaxiques et sémantiques strictes utilisées pour écrire des algorithmes et produire des logiciels.",
        "Un langage de programmation sert d'interface d'abstraction entre la logique humaine et le langage machine (binaire) exécuté par le processeur.",
        "C'est un système de notation formel conçu pour décrire des processus de traitement de l'information et des structures de données.",
        "Un langage de programmation est un outil de développement permettant de traduire des concepts logiques en fonctions exécutables par un ordinateur.",
        "Il se définit comme un vocabulaire et un ensemble de règles grammaticales destinés à commander le comportement d'un système informatique.",
        "Un langage de programmation est un vecteur d'automatisation qui permet de transformer des entrées de données en résultats spécifiques via des instructions structurées.",
        "Techniquement, c'est un langage formel qui permet de définir l'organisation de la mémoire, les calculs mathématiques et le flux de contrôle d'un programme.",
        "C'est un support d'expression technique qui permet aux développeurs de résoudre des problèmes complexes en les divisant en une suite d'instructions élémentaires.",
        "Un langage de programmation est une norme d'écriture qui permet d'assurer l'interopérabilité entre le développeur, le compilateur (ou interpréteur) et le matériel.",
    ],
    "python": [
        "super,je vois que tu veux apprendre le python ,alors commençons! le python est un langage de programmation puissant créé par Guido van Rossum,ce langage est dynamique et conseillé pour les débutants car il offre un conffort et des défis aux jeunes apprennants!voici quelques modules avec python:tkinter,pyttsx3,festapi,pyinstaller le module qui transorme un fichier python en une application exe!si tu es tenté par ce langage rend toi sur le site ruphy et apprend tous les langage que tu veux"
    ],
}

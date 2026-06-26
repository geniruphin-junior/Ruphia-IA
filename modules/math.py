import sympy as sp
import re
def executer_calcul_scientifique(message):
    """
    Module de calcul scientifique haute précision pour Ruphia.
    Gère l'algèbre, la trigo, les dérivées et les intégrales v3.O.
    """
    try:
        # 1. Nettoyage du message pour le rendre compréhensible par SymPy
        # On remplace les termes français par les fonctions SymPy
        calc_input = message.lower()
        replacements = {
            "calcule": "", "résous": "", "dérive": "diff",
            "intégrale de": "integrate", "racine de": "sqrt",
            "cosinus": "cos", "sinus": "sin", "tangente": "tan",
            "puissance": "**", "^": "**"
        }
       
        for word, replacement in replacements.items():
            calc_input = calc_input.replace(word, replacement)
       
        calc_input = calc_input.strip()
        # 2. Définition des symboles mathématiques standards
        x, y, z = sp.symbols('x y z')
        t = sp.symbols('t') # Utile pour la physique
        # 3. Transformation de la chaîne en expression SymPy
        # sympify est très puissant et sécurisé pour le calcul formel
        expr = sp.sympify(calc_input)
        # 4. Analyse du type de calcul demandé
        # Si l'utilisateur utilise "diff", on dérive. Sinon on simplifie/résout.
        if "diff" in calc_input:
            resultat = sp.diff(expr, x)
            prefixe = "La dérivée est : "
        elif "integrate" in calc_input:
            resultat = sp.integrate(expr, x)
            prefixe = "L'intégrale est : "
        else:
            # Tente de résoudre si c'est une équation (contient un égal) ou simplifie
            if "=" in calc_input:
                parties = calc_input.split("=")
                equation = sp.Eq(sp.sympify(parties[0]), sp.sympify(parties[1]))
                resultat = sp.solve(equation, x)
                prefixe = "Les solutions sont : "
            else:
                resultat = sp.simplify(expr)
                prefixe = "Résultat simplifié : "
        # 5. Formatage du résultat
        # On garde la forme mathématique propre (ex: sqrt(2) au lieu de 1.414)
        return f"{prefixe}{resultat}"
    except Exception as e:
        return "Je ne capte pas: Assurez-vous d'utiliser '*' pour multiplier (ex: 2*x) et '**' pour les puissances."
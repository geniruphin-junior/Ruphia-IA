import sympy as sp
import numpy as np
import re
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

def ruphia_ultra_engine(text):
    try:
        # 1. PRÉPARATION & NETTOYAGE
        q = text.lower().strip()
        t = standard_transformations + (implicit_multiplication_application, convert_xor)
        
        # 2. CONSTANTES PHYSIQUES ET MATHÉMATIQUES
        cst = {
            'pi': sp.pi, 'e': sp.exp(1), 'i': sp.I,
            'c': 299792458, 'g': 9.81, 'G': 6.67e-11,
            'h': 6.626e-34, 'na': 6.022e23,'c': sp.Symbol('c', real=True, positive=True),
    'g': sp.Symbol('g', real=True, positive=True),
    'G': sp.Symbol('G', real=True, positive=True),
    'h': sp.Symbol('h', real=True, positive=True),
    'hbar': sp.Symbol('hbar', real=True, positive=True),
    'kb': sp.Symbol('kb', real=True, positive=True),
    'na': sp.Symbol('na', real=True, positive=True),
    'me': sp.Symbol('me', real=True, positive=True),
    'qe': sp.Symbol('qe', real=True, positive=True),
        }
        

        # 3. MOTEUR STATISTIQUE AVANCÉ (Détection de listes [1, 2, 3])
        if "[" in q and "]" in q:
            list_str = re.search(r'\[.*\]', q).group()
            data = np.array(eval(list_str))
            return (f"📊 STATS RUPHIA :\n"
                    f"  - Moyenne  : {np.mean(data):.4f}\n"
                    f"  - Médiane  : {np.median(data)}\n"
                    f"  - Écart-type: {np.std(data):.4f}\n"
                    f"  - Somme    : {np.sum(data)}\n"
                    f"  - Étendue    : {np.ptp(data)}\n"
                    f"  - Variance   : {np.var(data):.4f}\n"
                    f"  - Q1 / Q3    : {np.percentile(data, 25)} / {np.percentile(data, 75)}")

        # 4. PRÉ-PROCESSING TRIGO (Degrés vers Radians)
        # Remplace 'sin(45deg)' ou 'sin 45 deg' par la version radians pour Sympy
        if "deg" in q:
            q = re.sub(r'(\d+)\s*deg', r'(\1*pi/180)', q)
        
        # Correction auto : 'sin5' -> 'sin(5)'
        q = re.sub(r'(sin|cos|tan|log|sqrt)(\d+)', r'\1(\2)', q)

        # 5. NETTOYAGE DES MOTS-CLÉS DE COMMANDE
        clean = q
        for v in ["calcule", "résous", "dérive", "intègre", "limite", "simplifie"]:
            if v in clean: clean = clean.split(v)[-1].strip()
        
        # 6. PARSING DE L'EXPRESSION
        expr = parse_expr(clean.replace('=', '-'), transformations=t, local_dict=cst)
        syms = list(expr.free_symbols)

        # 7. MOTEUR DE DÉCISION PUISSANT
        if any(w in q for w in ["dérive", "diff"]):
            var = syms[0] if syms else sp.Symbol('x')
            res = sp.diff(expr, var)
            sig = "Dérivation"
        elif any(w in q for w in ["intègre", "intégrale"]):
            var = syms[0] if syms else sp.Symbol('x')
            res = sp.integrate(expr, var)
            sig = "Intégration"
        elif any(w in q for w in ["résous", "solution", "solve"]):
            res = sp.solve(expr, syms)
            sig = "Équation(s)"
        else:
            # Simplification trigo et mathématique par défaut
            res = sp.simplify(sp.trigsimp(expr))
            sig = "Résultat Simplifié"

        # 8. FORMATTAGE DE SORTIE (Symbolique + Décimal)
        if hasattr(res, 'free_symbols') and not res.free_symbols:
            try:
                val_dec = float(res.evalf())
                final = f"{res} ≈ {val_dec:.6f}"
            except:
                final = res
        else:
            final = res

        return f"✨ RUPHIA ANALYSE [{sig}] -> {final}"

    except Exception as e:
        return f"❌ Erreur Ruphia : Analyse impossible ({str(e)})"

if __name__ == "__main__":
    print("═══ RUPHIA 4.0 : MOTEUR MATHÉMATIQUE ACTIF ═══")
    print("Mode : Sympy + Numpy | Stat, Trigo, Algèbre")
    while True:
        user_input = input("\n[KNG] Commande : ")
        if user_input.lower() in ['exit', 'quitter', 'q']: break
        print(ruphia_ultra_engine(user_input))
